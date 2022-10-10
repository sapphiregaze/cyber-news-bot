import os
import discord
import requests
from bs4 import BeautifulSoup

# rss feed of the news website
news = 'https://feeds.feedburner.com/TheHackersNews'

class MyClient(discord.Client):
    # print to terminal when the bot is active
    async def on_ready(bot):
        print('Currently logged in as ', bot.user)

    # client event to respond to messages
    async def on_message(bot, message):
        if message.author == bot.user:
            return
        if message.content == '$news':
            await message.channel.send(main())

# initialize the discord client
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

def main():
    # request the xml of the website and parse it with bs4
    source = requests.get(news)
    plaintext = BeautifulSoup(source.text, 'xml')

    # different type of data scraped from the xml stylesheet
    title = plaintext.find_all('title')
    publishDate = plaintext.find_all('pubDate')
    link = plaintext.find_all('link')
    
    # for each news get the title, date, and link
    for i, j, k in zip(title[1:4], publishDate[1:4], link[1:4]):
        print(i.text, j.text, '\n', k.text)
    
    return(i.text, j.text, '\n', k.text)

# call the main function
if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))