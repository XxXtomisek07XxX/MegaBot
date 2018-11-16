import discord
from.discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

import asyncio
import platform
import colorsys
import random
import os 
import time

import discord
from.discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='/')
client.remove_command('help')

@client.event
async def on_ready():
  print('The bot is ready!')
  print(bot.user.name)
  print(bot.user.id)
  
@client.command()
async def fakeban():
  await client.say('Dostal/a jsi ban! Ha jen si dělám standu :D')
  
@client.command()
async def support():
  await client.say('cms.megabot-support.webnode.cz')

@client.command()
async def discord():
  await client.say('https://discord.gg/9uer
N5z')

@client.command()
async def hosting():
  await client.say('****Zatím Žádný!****')
  
@client.command()
async def discordbot():
  await client.say('https://discord.gg/8dbfhWU')

client.run(os.getenv("BOT_TOKEN"))


