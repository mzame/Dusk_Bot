#Work with Python 3.6
import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = 'NTk5Mzk0NzI0NTE1ODA3MjQz.XSkl3A.PjG3cdmW_iF3k23FPe5-0qWtfuQ'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_roll(roll):
    if roll.author == client.user:
        return
    if roll.content.startswith('!roll'):
        possible_numbers = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        msg = 'You have rolled a' + random.choice(possible_numbers) + {roll.author.mention}.format(roll)
        await client.send_message(roll.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

client.run(TOKEN)
