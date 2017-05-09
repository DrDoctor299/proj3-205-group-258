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


#Removing number of messages.
@bot.command(pass_context = True)
async def clear(context, numberMessages : int):
    counter = 0
    async for current in bot.logs_from(context.message.channel, limit = numberMessages):
        if counter < numberMessages:
            await bot.delete_message(current)
            counter += 1
                #await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even

bot.run('Mjk5NTkwMTE3NzI5NzYzMzMx.C8gGzA.M1gH9w_XI_4iBKA9XsEhnUPm82w')