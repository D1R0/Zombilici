import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import platform
#from pathlib import Path #Optional

import os

prefix = str(os.environ.get("BOT_PREFIX"))

bot = commands.Bot(command_prefix='prefix')


@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Ready')
    print('--------')
    print('Credits D1R0')

    return await bot.change_presence(game=discord.Game(name="by D1R0"))

@bot.event
async def on_message(message):
    print(str(message.author)+":"+message.content)

bot.run(str(os.environ.get("BOT_TOKEN")))
