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

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

class toggle(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
          
def setup(bot):
  bot.add_cog(toggle(bot))
