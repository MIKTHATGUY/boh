import discord
import os
from discord.ext import commands

import time

client = commands.Bot(command_prefix = 'a!')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
       while 3 > 2:
        time.sleep(1)

        await message.channel.send('<@682692879776612355> SIMPPPP')





client.run('NjkyNjQwODkxODIyOTMyMDEw.XnxeGQ.yLu6YRc_R4sXHjyLS2xvY10H11k')