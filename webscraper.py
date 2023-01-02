import requests
from bs4 import BeautifulSoup

# rss feed of the news website
news = 'https://feeds.feedburner.com/TheHackersNews'

# request the xml of the website and parse it with bs4
source = requests.get(news)
plaintext = BeautifulSoup(source.text, 'xml')

# different type of data scraped from the xml stylesheet
title = plaintext.find_all('title')
publishDate = plaintext.find_all('pubDate')
link = plaintext.find_all('link')
description = plaintext.find_all('description')
image = plaintext.find_all('enclosure')

# the followings are functions that parse the data of an individual tag
def scrapeTitle(num):
    for i in title[num+1:num+2]:
        return i.text

def scrapeDate(num):
    for i in publishDate[num:num+1]:
        return i.text

def scrapeLink(num):
    for i in link[num+2:num+3]:
        return i.text

def scrapeDesc(num):
    for i in description[num+1:num+2]:
        return i.text

def scrapeImage(num):
    for i in image[num:num+1]:
        return i.get('url')

# stores the titles xml into a separate file
def writeTitle():
    file = open('.dat', 'w')
    file.write(scrapeTitle(0))
    file.close()

def compareTitle():
    file = open('.dat', 'r')
    content = file.readline()
    file.close
    if content == scrapeTitle(0):
        return True
    return False