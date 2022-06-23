from email.quoprimime import header_check
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import progressbar


# def get_position_link(url):
  
#   links = []
#   response = requests.get(url)
#   soup = BeautifulSoup(response.text)

#   a = soup.find_all('a', class_ = 'jobLink')

#   for i in a:
#     links.append('https://www.glassdoor.com' + i.get('href'))

#   return links

# get_position_link('https://www.glassdoor.com/Job/united-states-data-scientist-jobs-SRCH_IL.0,13_IN1_KO14,28.htm?sortBy=date_desc')


def get_position_link(url):

  links = []
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  a = soup.find_all('a', class_ = 'jobLink')

  for i in a:
    links.append('https://www.glassdoor.com' + i.get('href'))

  links = links[::3]

  return links

def get_all_links(num_page, url):
  link = []
  i = 1
  print('정보를 수집하고있습니다...')

  while i <= num_page:
    try:
      url_main = url + str(i) + '.htm?includeNoSalaryJobs=true#:~:text=11-,12,-13'
      link.append(get_position_link(url_main))
      print(url_main)
      i += 1
      time.sleep(0.5)
    except:
      print('정보 수집을 종료합니다.')
      break

  return link

##
url = 'https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14_IP'
links = get_all_links(3, url)

print(links[0][1])
print(links[1][1])
print(links[2][1])

https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14_IP14.htm?