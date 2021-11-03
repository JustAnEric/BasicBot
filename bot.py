import discord
import os
os.system("python setupfile.py &")
os.system("python zentools.py &")
from discord.ext import commands
from keep_alive import keep_alive
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

bot.run("YOUR_TOKEN_HERE")

# PLEASE NOTE: If you are using any public code editor, make sure the token is private. 
# Anyone can login and destroy your server through the bot.
