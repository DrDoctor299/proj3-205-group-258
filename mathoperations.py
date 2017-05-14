import discord
import asyncio
from discord.ext import commands

import json, requests
import urllib3
import googlemaps


description = '''  /direction /join /clear /chooselang '''
bot = commands.Bot(command_prefix='/', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    
TOKEN = "Your_token_here"

# Bot Adding
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
  
# Bot Subtracting
@bot.command() 
async def subtract(left : int, right : int):
    """Subtracts two numbers together."""
    await bot.say(left - right)

# Bot Dividing  
@bot.command() 
async def divide(left : int, right : int):
    """Divides two numbers together."""
    await bot.say(float (left / right)
    
#Math operation powers.
@bot.command()
async def tothepower(value : int, power : int):
    result = 1
    for x in range(0,power):
        result = result * value
    await bot.say(result)
    
bot.run(TOKEN)
