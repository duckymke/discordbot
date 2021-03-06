from datetime import date
from dates import dates
from random_dates import date_generator
import random

import discord
import os
from dotenv import load_dotenv

load_dotenv()


client = discord.Client() # creates a client which is basically a connection to discord

@client.event # registers an event
async def on_ready(): # this event is called when the bot is ready to be used
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # when the bot revies a message from the person this event is called andis triggered each time a message is received
    if message.author == client.user: # but if the message is from oursleves, we dont want the code to run so we return it
        return

    if message.content.startswith("$gimmedate"): # here the code checks to see if the message starts with a specific string to prompt the bot to reply
        date = date_generator(dates, "beep boop bap... the date generator ^tm has picked:")
        await message.channel.send(date)



client.run(os.getenv('TOKEN'))