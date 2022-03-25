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

    # print(message)

    if (message.author.id == 956370482582667265):
        date = date_generator(dates, "woah woah woah... Date Bot you suck. Here's a BETTER date B) ")
        await message.channel.send(date)


client.run(os.getenv('TOKEN2'))