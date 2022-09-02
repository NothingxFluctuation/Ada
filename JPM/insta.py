import requests
from bs4 import BeautifulSoup as bs
import json



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
}

# insta_url = 'https://www.instagram.com'
# insta_username = 'hassan.quaid'
# url = f"{insta_url}/{insta_username}/"
# response = requests.get(url, headers=headers)
# print(url, response.status_code)
# bs_html = bs(response.content, 'html.parser')
# infile = open('insta.html','w')

# # for link in bs_html.findAll('img'):
# #     infile.write(str(link))
# #     infile.write('\n')
# infile.write(str(bs_html))
# infile.close()


import os.path
# import requests 
# from bs4 import BeautifulSoup as bs


home ='https://www.instagram.com/'
username = 'hassan.quaid'
finalUrl = home + username + "/"

response = requests.get(finalUrl)  # Fetch the user's profile page

if response.ok:
    try:
        html = response.text
        soup = bs(html, features ="lxml") 
        soup_text = soup.text # Convert the entire page data in text string
        start_index = soup_text.find('profile_pic_url_hd')+21
        remaining_text = soup_text[start_index:] # rest of the data after 'profile_pic_url_hd":"'
        last_index = remaining_text.find('requested_by_viewer')-3
        image_url = remaining_text[:last_index]

        print("The image url is ", image_url)
    except:
        pass