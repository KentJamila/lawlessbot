import discord
import asyncio
import random
import time
import logging

#discord imports
from typing import List
from discord.ext.commands import Bot
from discord.ext import commands

class LRPAdmin:
    def __init__(self, bot):
        self.bot = bot

    def _member_has_role(self, member: discord.Member, role: discord.Role):
        return role in member.roles

    def _get_users_with_role(self, server: discord.Server,
                             role: discord.Role) -> List[discord.User]:
        roled = []
        for member in server.members:
            if self._member_has_role(member, role):
                roled.append(member)
        return roled

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, userName: discord.User):
        embed = discord.Embed(color = discord.Color(0).orange())
        await self.bot.kick(userName)
        embed.description = ":boot:: {} ".format(userName) + "has been kicked by {}".format(ctx.message.author.mention)
        await self.bot.say(embed=embed)

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, userName: discord.User and discord.Member):
        embed = discord.Embed(color = discord.Color(0).orange())
        await self.bot.ban(userName)
        embed.description = ":hammer:: {} ".format(userName) + "has been banned by {}".format(ctx.message.author.mention)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def prune(self, ctx, amount: int):
        embed = discord.Embed(color = discord.Color(0).orange())
        deleted = await self.bot.purge_from(ctx.message.channel, limit=amount)
        embed.description = "{} ".format(ctx.message.author.mention) + "has pruned {} message(s)".format(len(deleted))
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *args):
        embed = discord.Embed
        colors = {}
        if args:
            argstr = " ".join(args)
            if "-c " in argstr:
                text = argstr.split("-c ")[0]
                color_str = argstr.split("-c ")[1]
                color = colors[color_str]
            else:
                text = argstr
                color = discord.Color(0).red()
            await self.bot.delete_message(ctx.message)                
            await self.bot.say(embed=embed(color=color, description="**Server Admin {}:** ".format(ctx.message.author.name) + text))

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_permissions(administrator=True)
    async def dmrole(self, ctx: commands.Context, role: discord.Role, *, message: str):
        embed = discord.Embed(color = discord.Color(0).red())
        guild = ctx.message.server
        author = ctx.message.author
        try:
            await self.bot.delete_message(ctx.message)
            embed.description = "**Server Admin {}**".format(ctx.message.author.name) + " sent a message to {}".format(role.mention)
            await self.bot.say(embed=embed)
        except:
            pass
        dm_these = self._get_users_with_role(guild, role)
        for user in dm_these:
            try:
                await self.bot.send_message(user,
                                            message.format(user, role, author))
            except (discord.Forbidden, discord.HTTPException):
                continue

def setup(bot):
    bot.add_cog(LRPAdmin(bot))
    print("Admin Commands Ready")