# Cyber News Bot
## Descriptions

A discord bot that posts cybersecurity updates to a discord channel of your choice. Updates currently includes:

- Daily cyber news from **https://thehackernews.com/**
- Critical CVEs of varying severity

## Setup

Run the following command to clone the Github repository into your desired directory,

~~~
git clone https://github.com/SapphireGaze/cyber-news-bot
~~~

Then change directory into the repository, create a **.env** file
and add your discord bot token into the .env file like the following

~~~
TOKEN=YOUR_TOKEN
~~~

Then download the dependencies of the discord bot by running the following command,

~~~
pip install -r requirements.txt
~~~

Finally, go into main.py and change the **CHANNEL_ID** variable to the ID of the channel you want the bot to push updates in.

~~~
CHANNEL_ID = YOUR_CHANNEL_ID
~~~

## Execute the program

Run the following command.

~~~
python3 main.py
~~~

You're all set! Enjoy the bot!!