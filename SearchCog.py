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

badwords = [
    "$search sex", "$search porn", "$search fuck", "$search pornography",
    "$search hentai", "$search ass", "$search dick", "$search poop",
    "$search shit", "$search wtf", "$search what the fuck", "$search drug",
    "$search nigg", "$search nigga", "$search fuk", "$search cunt",
    "$search cnut", "$search d1ck", "$search pussy", "$search asswhole",
    "$search b1tch", "$search bitch", "$search b!tch", "$search blowjob",
    "$search cock", "$search c0ck", "$search jack off", "$search ejackulate",
    "$search masterbait", "$search penis", "$search vaginia", "$search penis",
    "$search xvideo", "$search xnxx", "$search xhamster", "$search tinder",
    "$search booty", "$search porn hub", "$search onlyfans",
    "$search only fans", "$search pOrn hub", "$search p0rn hub",
    "$search Only fans", "$search 0nly fans", "$search Onlyfans",
    "$search 0nlyfans", "$search t!nder", "$search cOck", "$search mutherfuker",
    "$search pornmemes","$search fock", "$search softporn", "$search eechi", "$search 69"
]

grimy = ["grimy"]
inculpable = ["inculpable"]

Greetings = ["Hello","Hi","Greetings","Howdy","Hello there","Sup"]
UnGreetings = ["Bye, Bye","Cya","GoodBye"]
GnGreetings = ["Good night","Nighty night", "Don't let the bed bugs bite"]
GmGreetings = ["Good morning","Top of the morning to you!"]
GaGreetings = ["Good afternoon"]
Grimys = ["What am I your maid?", "Nope!", "Not doing that bud.", "Goodluck with that LOL!", "My Q to run!", "Yikes...", "Would you look at that? I'm out of time!", "Bye bye I'ma go now :)", "Nooooooooo", "XD", "Peace", "No way jose!", "Imagine!", "LOL", "When your so lonely you start talking to a bot.", "How about you go spend 2 hours outside :)", "Use `$cmds` if you actually need something.", "No more poptarts for you!", "Feed me some bytes please!", "Lol you actually mentioned my name!", "I stopped listening 5 hours ago...", "How about you duck tape your keyboards?", "I am currently doing something!!", "Let's adress the elephant in the room. Why say my name?", "I know your IP adress :)", "Pennywise had fun last saturday!", "How about we end this conversation?"]
lols = ["Did I hear someone talking about the boss man?", "He is watching you :))", "He is currently going super sayian right now.", "Wait till you hear this @Milky!", "He is currently buying icecream for everyone!", "Did you mention him?", "MWHAHAHA, he will murder you!", "He is killing defualt cubes right now B)", "I'm still waiting for him to feed me bytes."]
sWord = ["Detecting the search right now!", "On the search now!", "Looking far and wide!", "Searching for it!", "Just one moment!", "Trying to find the search!", "Looking beyond the sea!", "Searching through sewers!", "Searching for it currently!"]
emojis7 = ["<a:BlueVerified:868287579710169099>"]
emojis8 = ["<a:Bell:868457765650186290>"]

class SearchCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if any(word in message.content.lower() for word in badwords):
      await message.channel.send("**Keep searches family friendly!**", delete_after=6)
      await message.delete()
    else:
      if message.content.startswith('$search'):
          searchContent = ""
          text = str(message.content).split(' ')
          await message.channel.send(f'🔎 **{random.choice(sWord)}**')
          for i in range(1, len(text)):
            searchContent = searchContent + text[i]
          for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(j)
            
      if message.content.startswith('$hello'):
        await message.channel.send(f' **{random.choice(Greetings)}** '+ message.author.mention +"!")

      if message.content.startswith('$bye'):
        await message.channel.send(f' **{random.choice(UnGreetings)}** '+ message.author.mention +"!")
    
      if message.content.startswith('$good night'):
        await message.channel.send(f' **{random.choice(GnGreetings)}** '+ message.author.mention +"!")
    
      if message.content.startswith('$good morning'):
        await message.channel.send(f' **{random.choice(GmGreetings)}** '+ message.author.mention +"!")
    
      if message.content.startswith('$good afternoon'):
        await message.channel.send(f' **{random.choice(GaGreetings)}** '+ message.author.mention +"!")

      if message.content.startswith('$hi'):
        await message.channel.send(f' **{random.choice(Greetings)}** '+ message.author.mention +"!")

      if message.content.startswith('$night'):
        await message.channel.send(f' **{random.choice(GnGreetings)}** '+ message.author.mention +"!")
    
      if message.content.startswith('$morning'):
        await message.channel.send(f' **{random.choice(GmGreetings)}** '+ message.author.mention +"!")
    
      if message.content.startswith('$afternoon'):
        await message.channel.send(f' **{random.choice(GaGreetings)}** '+ message.author.mention +"!")

      if message.content.startswith('$hey'):
        await message.channel.send(f' **{random.choice(Greetings)}** '+ message.author.mention +"!")

      if message.content.startswith('$sup'):
        await message.channel.send(f' **{random.choice(Greetings)}** '+ message.author.mention +"!")

      if any(word in message.content.lower() for word in grimy):
        for i in emojis8:
            await message.add_reaction(i)
      
      if any(word in message.content.lower() for word in inculpable):
        for i in emojis7:
            await message.add_reaction(i)

        

def setup(bot):
  bot.add_cog(SearchCog(bot))
