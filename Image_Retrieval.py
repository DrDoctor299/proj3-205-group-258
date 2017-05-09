import discord
from discord.ext import commands
import random
import urllib.request
from urllib.request import urlopen
import requests
from py_ms_cognitive import PyMsCognitiveWebSearch

@bot.command()
async def get_image(user_input:str):
    
    #storing the user input of the picture they want to get links of
    image_search="picture of" + user_input
    #This will search the internet with image search since it has the user input in it
    word_search = PyMsCognitiveWebSearch('3d2f4008e4f8429fba7dccb98e855743',image_search)
    #This will store the image search into imahe and gives it a limit of 20 possible images
    image = word_search.search(limit=20)
    
   #THe bot will retrieve these kind of like  aprint statement
    await bot.say(image[0].url)
    await bot.say(image[1].url)
 
