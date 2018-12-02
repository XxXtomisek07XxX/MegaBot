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
     print('The bot is ready!')
     print(bot.user.name)
     print(bot.user.id)
    
@bot.command(pass_context = True)
async def stop(ctx):
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await bot.say("Přestal jsem hrát v Roomce!")  
      



    

  
  
 
  
@bot.command()
async def fakeban():
  await bot.say('Dostal/a jsi ban! Ha jen si dělám srandu :D')
  
@bot.command()
async def support():
  await bot.say('megabot-support.webnode.cz')
 



                 



@bot.command()
async def hosting():
  await bot.say('https://github.com')
               
   
                

  
@bot.command()
async def discordbot():
  await bot.say('https://discord.gg/8dbfhWU')
  
@bot.command()
async def help():
        await bot.say("""Nápověda :question:  Aktuální prefix: ``/``

:joy: Zábava
``fakeban`` - dej si ban!
``meme`` - pošle vtipné meme
``osmball <otázka>`` - náhodně odpoví na tvou otázku
``dog`` - pošle náhodný obrázek psa
``cat`` - Pošle náhodný obrázek kočky
``asktrump`` - Zábavně ti odpoví na otázku
:pencil: General
``support`` - support stránka bota
``hosting`` - aktuální hosting bota
``discordbot`` - support server i pro ostatní boty
``ping`` - zobrazí ping bota
``userinfo <@hráč>`` - Zobrazí info o určeném (označeném) hráči
``server`` - Zobrazí Info o serveru

:key: Administrátor
``ban <@hráč>`` - zabanuje určeného (označeného) hráče
``mute <@hráč>`` - označený hráč nebude moct psát do chatu
``kick <@hráč>`` - vyhodí označeného hráče
``clear <počet zpráv>`` - smaže určený počet zpráv
``warn <@hráč>`` - varuje určeného (označeného) hráče
``unban <@hráč>`` - odbanuje určeného (označeného) hráče
``bans`` - list zabanovaných hráčů
``unmute <@hráč>`` - zruší u určeného (označeného hráče) mute

Před každý příkaz dejte prefix, ``/`` """)
       
@bot.command()
async def omfg():
     await bot.say("""Update 1.0.2🔔
     
     ``Nový Command cat``
     
     ``Nový Command asktrump``
     
     ****-Majitel Bota[Syn#1308]**** """)
     
     

 

   


        
        
        
   
        
   
      
     
        
            
               
              
              
                
               
 



   
  
    
    

    
    
                          
    
    
    
    
    
    
    
    
  
   
    
    
    
     
   
    
   
    
    
    
    
  
    
    
    
    
    
 
    
    
    
        

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def joinvoice(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await bot.join_voice_channel(channel)

      
                   
                   
                   
                   
        
     
        
        


        
        
      





 


 




 
 
 

 
 
 
 
 

 
 
 

 

 
 
    
    
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
     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Hráčské Info.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Jméno", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Nejvyšší Role", value=user.top_role)
    embed.add_field(name="Připojen", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


    
     

  
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, msg = None):
         await bot.delete_message(ctx.message)
         if not msg: await bot.say("Prosím řekněte co mam odeslat")
         else: await bot.say(msg)
         return


    




   
 
   

   
    



    


    

  


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
async def dog():
   import random 
     
   choices = ["https://cdn.discordapp.com/attachments/516330147813523458/516596610172715039/image0.jpg","https://cdn.discordapp.com/attachments/509349559194091536/516593490516377600/1543235858976311557054.jpg","https://cdn.discordapp.com/attachments/516330147813523458/516596627868352543/image0.jpg","https://cdn.discordapp.com/attachments/516330147813523458/516596610172715039/image0.jpg","https://cdn.discordapp.com/attachments/516330147813523458/516607563194957834/image0.png","https://cdn.discordapp.com/attachments/516330147813523458/516607530781376512/image0.jpg","https://cdn.discordapp.com/attachments/516330147813523458/516607505758158888/image0.jpg"]
             
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
    join.add_field(name = '__Majitel Serveru__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Lidé__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Role (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Vytvořeno: %s'%time);

    return await bot.say(embed = join);

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List Zabanovaných", description = x, color = 0xFFFFF)
    return await bot.say(embed = embed)

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await bot.get_bans(ctx.message.server)

    # Show banned users
    await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await bot.say('Ban list je Prázdný!.')
        return
    try:
        await bot.unban(ctx.message.server, ban_list[-1])
        await bot.say('Unbanovaný Hráč: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await bot.say('Nemáš práva.')
        return
    except discord.HTTPException:
        await bot.say('unban se nepovedl.')
        return
               
        	      	 		 		  

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Byl Odmutnut!", description="{0} Byl Unmutnut Administrátorem {1}!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="Nemáš na Unmute Práva!.", color=0xff00f6)
        await bot.say(embed=embed)



   
       
        
        
    





         
         
        
        


        
        
    
        
      


       
      
        
     



         
        
                 
         
   

    

@bot.command()
async def meme():    
   import random
   
   choices = ["https://cdn.discordapp.com/attachments/509349559194091536/516591058239488000/1543235275440-1393565654.jpg","https://cdn.discordapp.com/attachments/505786728678817794/513637645193183232/dxzlmdubvxy11.jpg","https://assets3.thrillist.com/v1/image/2766357/size/gn-gift_guide_variable_c.jpg","https://assets3.thrillist.com/v1/image/2766357/size/gn-gift_guide_variable_c.jpg","https://cdn.theatlantic.com/assets/media/img/mt/2018/05/shutterstock_297886754/lead_720_405.jpg?mod=1533691461"]
                                     
 
   await bot.say(random.choice(choices))

 
     
   
    

@bot.command(pass_context = True)
async def avatar(ctx, member: discord.Member):
    await bot.reply("{}".format(member.avatar_url))
 

       
@bot.command()
async def osmball():
     import random

     choices = ["Ano","Ne","Možná"]
   
     await bot.say(random.choice(choices))
       
@bot.command()
async def asktrump():
     import random
     
     choices = ["Ano!","Taco!!!","Kaufland!","Ne!","Trump!","Lídl!"]
     
     await bot.say(random.choice(choices))
     
@bot.command()
async def cat():
     import random
     
     choices = ["https://cdn.discordapp.com/attachments/487874661691162644/518119499837341716/IMG_20181130_184136.png","https://cdn.discordapp.com/attachments/517336481568653312/518122278656147478/sanel.jpg","https://cdn.discordapp.com/attachments/516363610415431683/518122740029587477/dad.jpg","https://cdn.discordapp.com/attachments/516363610415431683/518123103109382146/atat.jpg","https://cdn.discordapp.com/attachments/516363610415431683/518123349746909194/ada.jpg"]
      
     await bot.say(random.choice(choices))
                   
     
  
        
  
@bot.command()
async def thx():
     await bot.say('Ahoj!Na tomto Serveru není Administrátor Syn#1308! Pokud zde nebude bot Kicknut nebo práva Vráceny Tak Vám bot Může udělat Klidně i něco se Serverem děkuji za pochopení! -Majitel bota[Syn#1308]')

    
       
           
   
 
    
                  



    
  
    	
        
    
   
      
        
    
       
    
   
        
       		                  
                
              
   
    

   
  

       
            
       
   
    
        
    
       
     
   
       
      	                  
                
              
                
    
        
              
           
               









        

      
        
 
               
           
                
               
                 
               
         
                 
           
               
              
                
             

  
     

     

bot.run(os.getenv("BOT_TOKEN"))


