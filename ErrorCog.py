import discord
import os
import shutil
from discord.ext import commands
from discord.ext import commands, tasks
from main import commands
from discord.utils import get
import asyncio
import discord, requests, time, random
from discord.ext.commands import MissingPermissions
from googlesearch import search
import traceback
import sys

class ErrorCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          embed0 = discord.Embed(title ='You need to specify!', colour = discord.Colour.red())
          await ctx.send(embed=embed0, delete_after=5)
          await ctx.message.delete()
      elif isinstance(error, commands.MissingPermissions):
          embed1 = discord.Embed(title ='You need permissions!', colour = discord.Colour.red())
          await ctx.send(embed=embed1, delete_after=5)
          await ctx.message.delete()
      elif isinstance(error, commands.MissingRole):
          embed2 = discord.Embed(title ='You need a required role!', colour = discord.Colour.red())
          await ctx.send(embed=embed2, delete_after=5)
          await ctx.message.delete()
      elif isinstance(error, commands.BotMissingPermissions):
          embed3 = discord.Embed(title ="I don't have permissions!", colour = discord.Colour.red())
          await ctx.send(embed=embed3, delete_after=5)
          await ctx.message.delete()
      elif isinstance(error, commands.BotMissingRole):
          embed4 = discord.Embed(title ="I don't have the required roles!", colour = discord.Colour.red())
          await ctx.send(embed=embed4, delete_after=5)
          await ctx.message.delete()
      elif isinstance(error, commands.CommandOnCooldown):
          await ctx.send(ctx.message.author.mention + " **Your on cooldown! Try again in {:.2f}s**".format(error.retry_after), delete_after=5)
          await ctx.message.delete()
      raise error

def setup(bot):
  bot.add_cog(ErrorCog(bot))
