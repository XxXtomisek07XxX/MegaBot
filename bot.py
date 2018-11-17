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
  await bot.say('Dostal/a jsi ban! Ha jen si dělám standu :D')
  
@bot.command()
async def support():
  await bot.say('cms.megabot-support.webnode.cz')




                 



@bot.command()
async def hosting():
  await bot.say('****https://github.com/XxXtomisek07XxX/MegaBot****')
               
   
                

  
@bot.command()
async def discordbot():
  await bot.say('https://discord.gg/8dbfhWU')
  
 @client.command(pass_context=True)
async def help():
        embed = discord.Embed(
                 title = "Help"
                 description = """
                 Zde jsou všechny příkazy:
                 /fakeban 
                 Dostaneš ban xd
                  /Support
                 ------ Popisek------
                 /hosting
                 Ukáže ti to kde jostujeme bota.
                 /discordbot
                 -----------Popisek---------
                Příští update:
                /kick
                Vyhodí člověka ze serveru
                /ban
                Zabanuje člověka
                """
          color = discord.Color.green()
)
          await bot.say(embed=embed)  

bot.run(os.getenv("BOT_TOKEN"))


