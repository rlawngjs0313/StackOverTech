from bs4 import BeautifulSoup
import numpy as np
import requests
import time
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import re
import multiprocessing

def extract_link(bs4):

  bs4 = str(bs4)

  p1 = re.compile(r"\"like_count\":\s\d+,\s+\"id\":\s\d+")
  p2 = re.compile(r"\"id\":\s\d+")
  p3 = re.compile(r"\d+")

  ids = p1.findall(bs4)

  for i in range(len(ids)):
    ids[i] = p2.findall(ids[i])
  ids = sum(ids, [])

  for j in range (len(ids)):
    ids[j] = p3.findall(ids[j])
  ids = sum(ids, [])

  return ids

def get_position_link(url):

  links = []
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  #print(soup)
  ids = extract_link(soup)
  
  for i in ids:
    links.append("https://www.wanted.co.kr/wd/" + str(i))

  return links
  

def get_all_links(num,url):
  link = []
  i = 0
  print('collecting links....')

  while i <= num:
    try:
      url_main = url + str(i)
      #print(url_main)
      link.append(get_position_link(url_main))
      i += 20
      time.sleep(0.5)
    except:
      print('No more page found')
      break
  return link

def scrap_tech_stack(url):
  dic = {}
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  body = soup.find('body')


def get_count(num, p = 20):
  list = []
  allocate = int(num/p)
  for n in range (p):
    list.append(allocate)
  list[p-1] += num%p
  print("프로세스 할당량 : ", list)
  return list

if __name__ == '__main__':
  x = get_all_links(60,'https://www.wanted.co.kr/api/v4/jobs?1655965818429&country=kr&tag_type_ids=669&job_sort=company.response_rate_order&locations=all&years=-1&limit=20&offset=')
  print(x)