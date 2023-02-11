import requests
from bs4 import BeautifulSoup

# rss feed of the news website
news = 'https://feeds.feedburner.com/TheHackersNews'

def refreshFeed(tag):
    # request the xml of the website and parse it with bs4
    source = requests.get(news)
    plaintext = BeautifulSoup(source.text, features='xml')
            
    title = plaintext.find_all('title')
    publishDate = plaintext.find_all('pubDate')
    link = plaintext.find_all('link')
    description = plaintext.find_all('description')
    image = plaintext.find_all('enclosure')

    match tag:
        case 'title': return title
        case 'date': return publishDate
        case 'link': return link
        case 'description': return description
        case 'image': return image

# the followings are functions that parse the data of an individual tag
def scrapeTitle(num):
    title = refreshFeed('title')
    for i in title[num+1:num+2]:
        return i.text

def scrapeDate(num):
    publishDate = refreshFeed('date')
    for i in publishDate[num:num+1]:
        return i.text

def scrapeLink(num):
    link = refreshFeed('link')
    for i in link[num+2:num+3]:
        return i.text

def scrapeDesc(num):
    description = refreshFeed('description')
    for i in description[num+1:num+2]:
        return i.text

def scrapeImage(num):
    image = refreshFeed('image')
    for i in image[num:num+1]:
        return i.get('url')

# stores the titles xml into a separate file
def writeTitle():
    file = open('.dat', 'w')
    file.write(scrapeTitle(0))
    file.close()

# compare if the title stored in file is the same as current title
def compareTitle():
    file = open('.dat', 'r')
    content = file.readline()
    file.close
    if content == scrapeTitle(0):
        return True
    return False