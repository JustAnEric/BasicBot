import discord
import os
from setupfile import start_setup
os.system("python zentools.py &")
from discord.ext import commands
bot = commands.Bot(command_prefix="COMMAND_PREFIX_HERE")

@bot.event
async def on_connect():
  start_setup() # SETUP YOUR BOT
  print("Starting setup...")
  
# COMMANDS:

@bot.command()
async def test(ctx):
  print(f"test command executed from {ctx.guild}")
  await ctx.send("Test")
  
# RUN THE BOT:

bot.run("")

# PLEASE NOTE: If you are using any public code editor, make sure the token is private. 
# Anyone can login and destroy your server through the bot.
# If you are using a public code editor, try and find some details for keeping your bot token safe on that site.