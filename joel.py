import discord
from discord.ext import commands
import random
import urllib.request
from urllib.request import urlopen
import requests
from py_ms_cognitive import PyMsCognitiveWebSearch


description = '''/add , /multiply , /def_ret, /divide , /subtract , /roll , /choose , /repeat ,
/joined
                 .'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.command()
async def def_ret(user_input : str):
    t= user_input + "definition"
    
    #user_input=input() 
    #user_input1=user_input+t
    ##This will search using the websearch function for the definiton of the word
    word_search = PyMsCognitiveWebSearch('3d2f4008e4f8429fba7dccb98e855743',t)
    ##This will get the results from the search and save it into word_result
    word_result = word_search.search(limit=200)
   # await bot.say(print("Please enter the word you wish to find the definition for: "))
    #await bot.say(user_input=input())
    #await bot.say(user_input1=user_input+t)
    await bot.say(word_result[0].url)
    await bot.say(word_result[1].url)
