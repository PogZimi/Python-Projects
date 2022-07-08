#-----------------[Bot.py]-----------------------------

# Learn how to make a basic Discord bot in Python : 
# Published = 12/6/2022
# Author = Milo_Prysco

#----------------------------------------------------------

# Before using , please install discord API Wrapper by pasting this command in terminal -->  pip3 install discord 

import discord  # API Wrapper for discord

client = discord.Client(); # Client means our bot

# Creating Embed messages : 

myEmbed = discord.Embed(title = "Message type :  " , description = "Embed", color = 0x00ff00)
# Colour is in hexa decimal 
# Created first Embed , now lets implement it inside on_message(message) function, 

# Functions : 
@client.event 
async def on_ready():
     print("Logged in to our bot :  ", format(client)) 
     # Tells that we successfully logged in ...

@client.event
async def on_message(message):
     if message.author == client.user : # Means if the one who messages(is a bot) then dont reply 
        return 
     
     # Simple text messages
     if message.content.startswith("/hi"):
        await message.channel.send("Hello"); # Sends hello message when someday says /hi
     
     # Embed messages
     if message.content.startswith("/embed"): 
      myEmbed;
      myEmbed.add_field(name = "Bot Name :  ", value = "Basic_Bot_in_py", inline = False )
      myEmbed.add_field(name = "Bot Creator : ", value = "Milo", inline = False )
      myEmbed.set_footer(text = "MyBasicEmbed", icon_url = "https://images.unsplash.com/photo-1614680376739-414d95ff43df?fit=fillmax&fm=jpg&ixid=MnwzNTY3MHwwfDF8YWxsfHx8fHx8fHx8MTYxNzMyNjk2MA&ixlib=rb-1.2.1&q=75" );
      await message.channel.send(Embed = myEmbed); # Sends Embed message when we call "/embed" to channel                       
     

client.run('PASTE_YOUR_BOT_TOKEN'); # Runs our bot

# Inside the token paste the bot token needed to connect the code to bot so we can run this stuff, without token bot would not run
# Go to developer portal , create new application, create new bot, copy token & paste inside client.run('TOKEN');
