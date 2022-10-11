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
image = plaintext.find_all('media:thumbnail')

# for each news get the title, date, and link
def scrape():
    for i, j, k in zip(title[1:2], publishDate[1:2], link[1:2]):
        print(i.text, j.text, '\n', k.text)
    return (i.text, j.text, k.text)

# the followings are functions that parse the data of an individual tag
def scrapeTitle():
    for i in title[1:2]:
        return i.text

def scrapeDate():
    for i in publishDate[1:2]:
        return i.text

def scrapeLink():
    for i in link[1:2]:
        return i.text

def scrapeDesc():
    for i in description[1:2]:
        return i.text

def scrapeImage():
    for i in image[0:1]:
        return i.get('url')