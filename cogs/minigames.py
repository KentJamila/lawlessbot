import discord
import time
import asyncio
import random
import logging
import requests
import io
import safygiphy
import urllib
import aiohttp
import giphypop
import json
from discord.ext import commands
from imgurpython import ImgurClient
from discord.ext.commands import Bot
from discord import ChannelType
from discord.ext.commands import CommandError
import re

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tosscoin = [":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won", ":sun_with_face: Heads, congratulations to whoever won", 
":new_moon_with_face: Tails, congratulations to whoever won", ":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won", 
":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won"]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Minigamecommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def dice(self, ctx):
        embed = discord.Embed(color = discord.Color(0).orange())
        embed.description = "The dice landed on **{}**".format(random.randint(1, 6))
        await self.bot.say(embed = embed)
        
    @commands.command(pass_context = True)
    async def flip(self, ctx):
        embed = discord.Embed(color = discord.Color(0).orange())
        embed.description = random.choice(tosscoin)
        await self.bot.say(embed = embed)

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        embed = discord.Embed(color = discord.Color(0).orange())
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        embed.description = ":ping_pong: {}ms".format(round((t2-t1)*1000))
        await self.bot.say(embed=embed)

#----------------------------------------------------------OTHERCOMMANDS----------------------------------------------------------------------------------------------------
    @commands.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title="Bot Commands", color = discord.Color(0).orange())
        embed.description = """
```
Admin:
    ah            Admin Commands
Basic:
    dice          Roll a dice
    flip          Flip a coin
```
"""
        embed.set_footer(text="Bot by Lui")
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ah(self,ctx):
        embed = discord.Embed(title="Admin Commands", color = discord.Color(0).orange())
        embed.description = """
**Commands**
```
Admin:
    ?kick           <@user_name>
    ?ban            <@user_name>
    ?prune          <page(s)>
    ?announce       <text>
    ?dmrole         <@role> <message>
```
"""
        embed.set_footer(text="Bot by Lui")
        await self.bot.say(embed=embed)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setup(bot):
    bot.add_cog(Minigamecommands(bot))
    print("minigames")