import os
import discord
from discord.ext import commands
import webscraper
from dotenv import load_dotenv

# load discord token from .env
load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

# set command prefix and intents
intents = discord.Intents.default()
intents.message_content = True

bot  = commands.Bot(command_prefix='/', intents=intents)

# print to terminal and store data in .dat when the bot is active
@bot.event
async def on_ready():
    print('Currently logged in as', bot.user)
    webscraper.data(0)

# return the number of news articles that the user requested
@bot.command(name='news')
async def cyber_news(ctx, arg: int):
    for num in range(arg):
            embed=discord.Embed(title=webscraper.scrapeTitle(num), url=webscraper.scrapeLink(num), color=discord.Color.purple())
            embed.set_thumbnail(url=webscraper.scrapeImage(num))
            embed.add_field(name="Description:", value=webscraper.scrapeDate(num)+'\n'+webscraper.scrapeDesc(num), inline=False)
            await ctx.channel.send(embed=embed)

# start the bot process
if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)