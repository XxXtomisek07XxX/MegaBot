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
     await bot.change_presence(game=discord.Game(name= "/help"))
     
   
        

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
        await bot.say("""****__Nápověda :mailbox_with_mail:__****       ****Prefix:/****
        
        
        
      

****Zábava**** :joy:

``` fakeban
 meme```

****General**** :pencil:

``` support
 hosting
 discordbot
 ping```
 
 
 ****Administrátor**** :key:
 
``` ban
 mute
 kick
 clear
 warn``` """)
 
    
    
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

  

    


@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content=':ping_pong: Ping: {}ms'.format(int(ms)))
      


@bot.command(pass_context = True)
async def warn(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await bot.say(ctx.message.author.mention +  " Označ Uživatele!")
    try:
        await bot.warn(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await bot.say("Dostal jsi Warn!")
 
    embed = discord.Embed(description = "%s Dostal jsi warn!"%member.name, color = 0xF00000)
    return await bot.say(embed = embed)
   

   
    



    


    

  


@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User byl Mutnut!", description="{0} dostal/a jsi mute od {1}!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed = embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="Nemáš práva na mute a nebo Je Daný člověk Administrátor.", color=0xff00f6)
        await bot.say(embed = embed)




      
                
             
@bot.command()
async def meme():   
   import random

   choices = ["https://cdn.theatlantic.com/assets/media/img/mt/2018/05/shutterstock_297886754/lead_720_405.jpg?mod=1533691461","https://assets3.thrillist.com/v1/image/2766357/size/gn-gift_guide_variable_c.jpg"]
             

   
   await bot.say(random.choice(choices))
            
               
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  

async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await bot.delete_messages(mgs)          
        await bot.say(str(number)+' Zprávy Smazány')
     
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('clear se Nepodařilo.')
        return         
   
 
    await bot.delete_messages(mgs) 
                  
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)    

async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await bot.change_nickname(user, nickname=nickname)
    role = bot.utils.get(ctx.message.server.roles, name='Administrative Department')
    await bot.remove_roles(user, role)
    await bot.delete_message(ctx.message)

async def server(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await bot.say(embed = join);


               
                
              
                
    
        
              
           
               









        

      
        
 
               
           
                
               
                 
               
         
                 
           
               
              
                
             

  
     

     

bot.run(os.getenv("BOT_TOKEN"))


