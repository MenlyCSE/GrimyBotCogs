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

class MiscCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['Item'])
  @commands.cooldown(1,3,commands.BucketType.user)
  async def item(self, ctx):
    await ctx.send(f'Your lucky item is **{random.choice(tickets)}**')

  @commands.command(aliases=['Predict'])
  @commands.cooldown(1,3,commands.BucketType.user)
  async def predict(self, ctx):
    await ctx.send(f'I predict **{random.choice(predictions)}{random.choice(puncuations)}**')

  @commands.command(aliases=['Crystal'])
  @commands.cooldown(1,3,commands.BucketType.user)
  async def crystal(self, ctx):
    await ctx.send(f'The crystalball says **{random.choice(crystalball)}{random.choice(puncuations2)}**')

  @commands.command(aliases=['Misc'])
  @commands.cooldown(1,10,commands.BucketType.user)
  async def misc(self, ctx):
    await ctx.send(embed=embed11)

puncuations = ['.','!','!?','...']
puncuations2 = ['.','!',' :0','...',' :)',' :D']

predictions = ['Blender will soon have multiplayer mode','drip goku meme will never die','frieza will actually kill goku','Roblox stock price will be at $250 dollars','America might survive the tsunami that will occur in 2025','google will still be alive','robots will rule the world','gas prices will be $500','amazon will shut down','walmart will dominate the market','red bull will actually give you wings','wars will occur','Inculpable will make decent animations','Grimy - Blend will grow massively','an astroid will hit your house','tiktok will take over YouTube','someone will hack the pentagon','we all will get free nitro','discord will still be alive','Blender will beat any paid 3D programs','frozen 4 will release','cartoons will be come animes','protest for Blender civil rights might happen','you will use the command $item','nothing']

crystalball = ['you will be a hero in the future','you will be goku','you will figure out anime portals','you will master a sector of blender','you will go super sayian 15','you will own 15 bag of carpets','you will have key chains','you will eat a sandwich today','you will try alvacado with bread and will love it','you will have a normal day','you will not see a alagator','you will be reading this message','you will use bing','you will throw away duckduckgo','you will brush your teeth tonight','you will enjoy dinner','you will hack the pentagon','you will discover YouTube secrets','you will have powers in 1 million years','you will buy a vr headset','you will destroy some kids at soccer','you will delete fortnite','you will enjoy Roblox','you will win 1 million vBux but then loose it because you took to long to claim','you will never get nitro']

tickets = ['500 rottem apples!','a snake.','2 poison frogs.','1 defualt cube!!!','1 million dollars!','a dead business.','a expired credit card :(','2 robux xD!','15 defualt cubes :D','a penny :)', 'a kickstar account!','6 dragon balls.','15 blender add ons.','2 bad contents.','unlucky penny :C','a stick.','honey on toast!','5 packs of ham.','a cheese :)','a walmart shopping list.','$-15.','soupereme basket B)','2 diss tracks!','a crown.','3 goldfish.','1 gallon of water.','a donut.','a ripped mask.','2 pairs of skinny jeans!','a sledge hammer O_O','1 ounce of butter.','half a cheesecake!','2 lotion bottles.','1 computer charger -_-','3 soda bottles empty.','3 broken lamps.','1 illegal lamborghini :0','red bull that will not give wings!','half a headphone.','2 windex bottles filled with water.']

embed11 = discord.Embed(
  title = '**Fun commands!**',
  description = 'These are commands used for fun!\nFeel free to play around with them.',
  colour = discord.Colour.green()
)

embed11.add_field(name = 'All fun commands', value = '`$predict` to predict the future!\n`$item` to pull a random item!\n`$crystal` To predict your future!\n`$play` to play with Grimy!')

def setup(bot):
  bot.add_cog(MiscCog(bot))
