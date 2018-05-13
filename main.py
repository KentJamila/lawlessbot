#LUI DRAYTON - LAWLESS ROLEPLAY
#Musika Creator

import discord
import time
import random
import logging
import giphypop
import safygiphy
import dbl
import aiohttp
import sys
import traceback
import sqlite3
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import command
import discord.errors
import discord.ext
from tabulate import tabulate
from discord.utils import find

startup_extensions = ["cogs.lawlessadmin", "cogs.minigames"]

bot = commands.Bot(command_prefix="?")
bot.remove_command('help')

@bot.event
async def on_command_error(error, ctx):
    embed = discord.Embed(color = discord.Color(0).orange())
    channel = ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        embed.description = ":thinking: Command not found - ?help for command list"
        await ctx.bot.send_message(channel, embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='samp.lawlessrp.com'))
    
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc ='{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run("token")
