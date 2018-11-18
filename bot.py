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
bot.remove_command('help')


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
  await bot.say('https://github.com/XxXtomisek07XxX/MegaBot')
               
   
                

  
@bot.command()
async def discordbot():
  await bot.say('https://discord.gg/8dbfhWU')
  
@bot.command()
async def help():
        await bot.say("""****__prefix:/__****

****Zábava****

``` fakeban```

****General****

``` support
 hosting
 discordbot``` """)
    
    
@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await bot.say('**Nemáš Oprávnění na kick a nebo je dotyčný Administrátor**')
        return
    
    try:
        await bot.kick(user)
        await bot.say(user.name+' byl kicknut. Měj se '+user.name+'!')
        await bot.delete_message(ctx.message)

    except discord.Forbidden:
        await bot.say('Permission denied.')
        return
   
    

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True) 

async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await bot.say('**Nemáš Právo na ban a nebo je dotyčný Administrátor!**')
        return

    try:
        await bot.ban(user)
        await bot.say(user.name+' byl Zabanován. Měj se '+user.name+'!')

    except discord.Forbidden:

        await bot.say('Permission denied.')
        return
    except discord.HTTPException:
        await bot.say('Ban nebyl Úspěšný.')
        return		 

  

    



      


    
   

   
    



    


    

  


@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="{0} was muted by {1}!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed = embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed = embed)




      
                
             

               
               

                  

               
                
              
                
    
                
              
           
               



        


        

      
        
 
               
           
                
               
                 
               
         
                 
           
               
              
                
             

  
     

     

bot.run(os.getenv("BOT_TOKEN"))


