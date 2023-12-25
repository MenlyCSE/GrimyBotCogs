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

class AdminCogs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(kick_members=True)
  async def purge(self, context, amount=5):
      await context.channel.purge(limit=amount+1)
      await context.send("**Purge done!**", delete_after=5)
      await context.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(kick_members=True)   
  async def kick(self, context, member : discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await context.send(f'{member} **Was thrown off the rail!**')
      await context.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(ban_members=True)   
  async def ban(self, context, member : discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await context.send(f'{member} **Has been banished!**')
      await context.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(ban_members=True)   
  async def unban(self, context, id : int):
      user = await commands.fetch_user(id)
      await context.guild.unban(user)
      await context.send(f'{user.name} **Is now unbanished!**')
      await context.message.delete()
      
  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(ban_members=True)
  async def softban(self, context, member : discord.Member, days, reason=None):
      days * 86400 
      await member.ban(reason=reason)
      await context.send(f'{member} **Is temporarily railed off!**')
      await asyncio.sleep(days)
      print("Time to unban")
      await member.unban()
      await context.send(f'{member} **has completed the banish time!**')
      await context.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member : discord.Member):
      guild = ctx.guild
      
      for role in guild.roles:
          if role.name == 'Muted':
              await member.add_roles(role)
              await ctx.send('{} **Is now duck taped!**'.format(member.mention))
              await ctx.message.delete()
              return
              
              overwrite = discord.PermissionsOverwrite(send_messages=False)
              newRole = await guild.create_role(name='Muted')
              
              for channel in guild.text_channels:
                  await guild.set_permissions(newRole,overwrite=overwrite)
                  
              await member.add_roles(newRole)
              await ctx.send('{} **Is now duck taped!**'.format(member.mention))
              await ctx.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member : discord.Member):
    guild = ctx.guild
    for role in guild.roles:
      if role.name == 'Muted':
        await member.remove_roles(role)
        await ctx.send('{} **Is now free of speech!**'.format(member.mention))
        await ctx.message.delete()

  @commands.command()
  @commands.Cog.listener()
  @commands.has_role("Event Manager")
  async def eventoff(self, ctx, channel : discord.TextChannel=None):
    
    embed20 = discord.Embed(title = 'Events are currently closed! Winners will be announced!', colour = discord.Colour.red())
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.message.delete()
    await ctx.send(embed=embed20)

  @commands.command()
  @commands.Cog.listener()
  @commands.has_role("Event Manager")
  async def eventon(self, ctx, channel : discord.TextChannel=None):


    embed24 = discord.Embed(title = 'Events are currently opened! You may enter in now!', colour = discord.Colour.blue())
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.message.delete()
    await ctx.send(embed=embed24)

      
def setup(bot):
  bot.add_cog(AdminCogs(bot))
