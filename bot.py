import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

import asyncio
import platform
import colorsys
import random
import os 
import time





bot=commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
  print('The bot is ready!')
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command()
async def fakeban():
  await client.say('Dostal/a jsi ban! Ha jen si dělám standu :D')
  
@bot.command()
async def support():
  await client.say('cms.megabot-support.webnode.cz')




                 



@bot.command()
async def hosting():
  await client.say('****Zatím Žádný!****')
  
@bot.command()
async def discordbot():
  await client.say('https://discord.gg/8dbfhWU')

client.run(os.getenv("BOT_TOKEN"))


