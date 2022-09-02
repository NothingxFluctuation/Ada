from .models import Technology, HLF
from .scrapy import scraper
import time




headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': 'https://example.com',
  'cookie': """your cookie value ( you can get that from your web page) """
}

def main_scraper():

    MAIN_QUERY_URL = "https://www.indeed.com/jobs?q=" #US
    # MAIN_QUERY_URL =  "https://au.indeed.com/jobs?q=" #AU
    # MAIN_QUERY_URL = "https://ca.indeed.com/jobs?q=" #CA


    technologies = Technology.objects.all()

    for tech in technologies:
        print("Fetching Technology: ", tech)
        for filter in HLF.objects.all():
            print("Applying Filter: ", filter.filter_name)
            print("MAIN_QUERY_URL", MAIN_QUERY_URL)
            main_url = MAIN_QUERY_URL + tech.name + filter.filter_url + "&fromage=" + filter.days
            print("Started the scraper: ", main_url)
            time.sleep(3)
            scraper(tech.name, main_url, filter.filter_name, filter.filter_name)

