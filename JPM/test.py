import requests
from bs4 import BeautifulSoup
import time

MAIN_URL = "https://www.indeed.com/jobs?q=django&l&sc=0kf%3Aattr(DSQF7)jt(contract)%3B&vjk=c863b057044219e8&sort=date"


def scraper(main_url):
    pagination = None
    blue = main_url
    while main_url:
        print("Fetching page...", main_url)
        page = requests.get(main_url)
        print("Page Fetched.")
        bsObj_page = BeautifulSoup(page.content, 'html.parser')
        # print("BeautifulSoup Object Created.")
        # print("Iterating through BeautifulSoup Object.")
        # for jobCard in bsObj_page.findAll('div',{'class':'job_seen_beacon'}):
        #     job_title = jobCard.find('a',{'class':'jcs-JobTitle'}).get_text()
        #     job_id = jobCard.find('a',{'class':'jcs-JobTitle'})['data-jk']
        #     job_url = 'https://www.indeed.com/viewjob?jk=' + job_id
        #     print("Current Job: ", job_title, " URL: ", job_url)
        #     company_name = jobCard.find('span',{'class':'companyName'}).get_text()
        #     posted = jobCard.find('span',{'class':'date'}).get_text()
        #     print("Company Name: ", company_name, "Posted On: ", posted)
        #     print("Saved in DB.")

        # try:
        # print("blue: ",bsObj_page.find('ul',{'class':'pagination-list'}).findAll('li'))
        pagination_length = len(bsObj_page.find('ul',{'class':'pagination-list'}).findAll('li'))
        print("my pagination length: ", pagination_length)
        # next_page = bsObj_page.find('ul',{'class':'pagination-list'}).findAll('li')[count + 1].a['href']
        # main_url = 'https://www.indeed.com' + next_page
        # count += 1
        # print("Let's go to the next page: ", main_url)
        # time.sleep(2)
        if pagination_length <= 1:
            break

        if pagination == None:
            pagination = list((range(10, pagination_length * 10 - 10, 10)))
            print("paginationo: ", pagination)

        if len(pagination) == 0:
            break


        main_url = blue + "&start=" + str(pagination[0])
        pagination.pop(0)

        # except:
        #     print('Pages Ended.')
        #     main_url = None


scraper(MAIN_URL)