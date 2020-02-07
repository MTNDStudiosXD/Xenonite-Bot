import discord
from discord.ext import commands
import asyncio
import keep_alive
import os
#------------------------------------
from discord.ext import *
from discord.ext import commands
#-------------------------------------

print("Bot loading...")

bot = commands.Bot(command_prefix='x!') #prefix
bot = commands.Bot(command_prefix='oof') #prefix
bot.remove_command:help

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name="wtf do u want", url="https://www.youtube.com/watch?v=WtKWtY5cyiU"))
  print(f"Bot is online!") # Shows on the console that the bot is working.


@bot.command(pass_text=True)
async def gay(ctx):
    await ctx.send('no u')
    print ("Typing no u....")

@bot.command(pass_text=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    print ("Purging Channel....")
    await ctx.send ('Cleared.')

@bot.command(pass_text=True)
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=100000000000):
    await ctx.channel.purge(limit=amount)
    print ("Nuking Channel....")
    await ctx.send ('Channel Nuked.')
    
@bot.command(pass_text=True)
async def ban(ctx, member):
  await ctx.send ("**This Command Has Been ``||Permenantely||`` Removed, It is NOT Working and It has plenty of Errors.**")

@bot.command(pass_text=True)
async def kick(ctx, member):
  await ctx.send ("**This Command Has Been ``||Permenantely||`` Removed, It is NOT Working and It has plenty of Errors.**")

@bot.command(pass_text=True)
async def say(ctx, message):
  await ctx.message.delete()
  await ctx.send(message)

keep_alive.keep_alive()
token = os.environ.get("BOT_TOKEN_HERE")
bot.run(token, bot= True, reconnect=True) 