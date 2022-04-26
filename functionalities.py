import discord
import os
import sys
import time

class Main:
  # CHANGE PRESENCE;
  @staticmethod
  async def presence_change(activity, status, bot:discord.Client):
    await bot.change_presence(activity, status, afk=False)
    print("Changed status by the power of discord.Client()")
    
  # FETCH GUILD BY ID;  
  @staticmethod
  async def s_fetch(bot, server_ID:int):
    await bot.get_guild(server_ID)
    
# DO NOT EDIT THIS, COPY THIS, OR USE THIS IN YOUR OWN SCRIPT. YOU ARE ALLOWED TO MODIFY, ADD, CHANGE STUFF IN THIS SCRIPT; BUT RELEASING IT UNDER YOUR OWN NAME IS FORBIDDEN.
# TO USE THIS BOT TEMPLATE, YOU MUST AGREE TO ALL OF THE ABOVE. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^;
