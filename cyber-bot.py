import os
import discord
import webscraper

class MyClient(discord.Client):
    # print to terminal when the bot is active
    async def on_ready(bot):
        print('Currently logged in as', bot.user)

    # client event to respond to messages
    async def on_message(bot, message):
        if message.author == bot.user:
            return
        if message.content == '!news':
            embed=discord.Embed(title=webscraper.scrapeTitle(), url=webscraper.scrapeLink(), color=discord.Color.purple())
            embed.set_thumbnail(url=webscraper.scrapeImage())
            embed.add_field(name="Description:", value=webscraper.scrapeDate()+'\n'+webscraper.scrapeDesc(), inline=False)
            await message.channel.send(embed=embed)
        
# initialize the discord client & intent
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# start the bot process
if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))