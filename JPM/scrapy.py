import requests
from bs4 import BeautifulSoup
from .models import BlackBall, JobPost, GStack
import time
import re

# cookies = {
#     'CO': 'US',
#     'CSRF': 'srwycOYfojUg0sbDDZ0kJoyeJ7WbzEEZ',
#     'CMP_VISITED': '1',
#     'CTK': '1fspfpbjdu211800',
#     'INDEED_CSRF_TOKEN':'raGlx1bH8qlB6A31273rrF6qH9Dk7Vvs',
#     'JSESSIONID':'916531FDA189AA9E4CE0B48A1E1BCE94',
#     'LV': '=1655862675:CV=1656458313:TS=1645827894"',
#     'PREF':'"TM=1655153713225:L="',
#     'RQ':'ails&l=New+York%2C+NY&ts=1645827900495"',
#     'UD':'ails&l=New+York%2C+NY&ts=1645827900495"',
#     '_dd_s':'rum=0&expire=1661834977487',
#     'ac':'DCl2wCgdEe2c2xuPjmEbCA#DCoTACgdEe2c2xuPjmEbCA',
#     'LC': '"co=US&hl=en"',
#     'LOCALE': 'en',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Jul+26+2022+20%3A17%3A32+GMT-0400+(Eastern+Daylight+Time)&version=6.37.0&isIABGlobal=false&hosts=&consentId=7b9d0af9-c7f4-468c-ad75-7d36e806cdfd&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false',
#     'PPID': '',
#     'RF': 'mUhsjgfUcbEpMQQmFzF8MPcEwAA3Un7m1seYpdEcJU41eWZ5GZ5bTgKgrdYuby3nlnXwzbs6tnZUBZpjlwKVBiKIRvr3VWJuOXxtBYZBFK4="',
#     'SHARED_INDEED_CSRF_TOKEN': 'Q5eNL764Vh53513rvrVm85gGlxuOTUPM',
#     '_cf_bm': 'jE_jprY0EuDgxdUwt7e0YRwRzSD7KOc6fGedQAPg8kM-1658880510-0-AdXvm3p5WMw9RdcpZMnGqfyI2zIovl3GLFeto15eDcTY66/K+rOFwAJ0/BZbSbqLDONPJwleOcLjQbri9D260BM=',
#     '_ssid': '7aa9e35368aa8a4353a8233c750b3a3,',
#     '_cfuvid': 'CS6X4Ic61KD70E7ZXlrR7uBWNVsjuw54plCzlHDBIbs-1658880510609-0-604800000',
#     '_ga': 'GA1.2.978787428.1654904744',
#     '_gcl_au': '1.1.474910968.1654915934',
#     'g_state': '{"i_l":0}',
#     'gonetap': '2',
#     'indeed_rcc': 'LOCALE:PREF:LV:CTK:CO:UD:RQ',
# }

cookies = {}



headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

def JPSaver(job_url):
    page = requests.get(job_url, headers=headers, cookies=cookies)
    bsObj = BeautifulSoup(page.content, 'html.parser')
    result = {}
    try:
        result['q'] = bsObj.find('div',{'id':'qualificationsSection'}).get_text()
    except:
        result['q'] = None
    try:
        result['d'] = bsObj.find('div',{'id':'jobDescriptionText'}).get_text()
    except:
        result['d'] = None

    return result


def CPQuantify(job_post):
    content =  job_post.title.lower().split(' ') + job_post.content.lower().split(' ')
    stacks = GStack.objects.all()
    cp = 0.0
    for stack in stacks:
        count = content.count(stack.name.lower())
        print('GS: ', stack.name,' Count: ', count)
        cp += job_post.cp + (count * stack.p)
    print('CP: ', cp)
    job_post.cp = cp
    job_post.save()


def BlackBallCheck(job_post):
    content = job_post.title.lower() + ' ' + job_post.content.lower()
    blackballs = BlackBall.objects.all()
    for blackball in blackballs:
        if blackball.tech:
            if blackball.title:
                if blackball.word:
                    if blackball.name.lower() in job_post.title.lower().split(' '):
                        job_post.garbage = True
                else:
                    if blackball.name.lower() in job_post.title.lower():
                        job_post.garbage = True
            else:
                if blackball.name.lower() in content:
                    job_post.garbage = True
        else:
            if blackball.name.lower() in content:
                job_post.bgc = True
    job_post.save()



def scraper(tech, main_url, jt, loc):
    print("Received: ", main_url)
    print("Fetching page...")
    page = requests.get(main_url, headers=headers, cookies=cookies)
    print('page: ', page)
    pagination = None
    while page:
        print("Page Fetched.")
        bsObj_page = BeautifulSoup(page.content, 'html.parser')
        print("BeautifulSoup Object Created.")
        print("Iterating through BeautifulSoup Object.")
        try:
            for jobCard in bsObj_page.findAll('div',{'class':'job_seen_beacon'}):
                job_title = jobCard.find('a',{'class':'jcs-JobTitle'}).get_text()
                job_id = jobCard.find('a',{'class':'jcs-JobTitle'})['data-jk']
                job_url = 'https://www.indeed.com/viewjob?jk=' + job_id #US
                # job_url = 'https://au.indeed.com/viewjob?jk=' + job_id #AU
                # job_url = 'https://ca.indeed.com/viewjob?jk=' + job_id #CA


                print("Current Job: ", job_title, " URL: ", job_url)
                company_name = jobCard.find('span',{'class':'companyName'}).get_text()
                posted = jobCard.find('span',{'class':'date'}).get_text()

                if len(JobPost.objects.filter(url=job_url)) > 0:
                    print("Already exists in DB.")
                    pass
                

                else:
                    time.sleep(2)
                    print("Fetching Job: ", job_url)
                    job_details = JPSaver(job_url)
                    jp = JobPost.objects.create(title = job_title,
                                            url = job_url,
                                            job_type = jt,
                                            company_name = company_name,
                                            location = loc,
                                            qualification = job_details['q'],
                                            content = job_details['d'],
                                            posted_on = posted,
                                            )
                    CPQuantify(jp)
                    BlackBallCheck(jp)
                    print("Saved in DB.")
        except:
            pass
        try:
            next_page = bsObj_page.find('ul',{'class':'pagination-list'}).findAll('li')[1].a['href']
            pagination_length = len(bsObj_page.find('ul',{'class':'pagination-list'}).findAll('li'))
            if pagination_length < 1:
                break
            if pagination == None:
                pagination = list(range(10, pagination_length * 10 - 10, 10))
            
            if len(pagination) == 0:
                break

            # print("bullshit")
            next_page = main_url + "&start=" + str(pagination[0])
            pagination.pop(0)
            page = requests.get(next_page, headers=headers, cookies=cookies)
            print("Let's go to the next page: ", next_page)
            time.sleep(3)

        except:
            print('Pages Ended.')
            page = None