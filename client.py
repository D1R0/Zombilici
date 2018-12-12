import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import platform
from discord.utils import get
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

    return await bot.change_presence(game=discord.Game(name=str(os.environ.get("NAME_TOKEN"))))

@bot.event
async def on_member_join(member):
    server = '522330800805511169'
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}, please read the rules and enjoy your stay.'
    await bot.send_message(server, fmt.format(member, member.server))
    
async def on_member_remove(member):
    server = '522330800805511169'
    fmt = '{0.mention} has left/been kicked from the server.'
    await bot.send_message(server, fmt.format(member, member.server))
    
async def on_message(message):
    print(str(message.author)+":"+message.content)
    
    if message.content == "accept":
        role = get(message.server.roles, id='519103654616367114')
        if not role in message.author.roles:
            await bot.send_message(message.author, "Bine ai venit pe ***☣ Zmbio Community ☣***!")
            await bot.wait_until_ready()
            await bot.add_roles(message.author, role)
            await bot.delete_message(message)

    if message.content.startswith("https://discord.gg/:"):
        await bot.delete_message(message)

    if message.content.startswith("discord.gg/"):
        await bot.delete_message(message)
            
bot.run(str(os.environ.get("BOT_TOKEN")))
