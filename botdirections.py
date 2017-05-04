import discord
import asyncio
from discord.ext import commands

import json, requests
import urllib3
import googlemaps


description = '''  /direction /join  '''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def join(URL : str):
    """Opens a stream player to youtube."""
    channel = bot.get_channel('298743472490414084')
    voice = await bot.join_voice_channel(channel)
    player = await voice.create_ytdl_player(URL)
    player.start()


@bot.command()
async def direction(userStart : str, userFinish : str, myMode : str, myLanguage): 
#Google Directions API in Python

    directions ='https://maps.googleapis.com/maps/api/directions/json'
    
    #directions. One of "driving", "walking", "bicycling" or "transit"
    #language ca,en,de,ar,fr,es.
    param = {'origin': userStart, 'destination': userFinish , 'mode': myMode, 'language': myLanguage , 'optimize_waypoints': True, 'alternatives': True, 'key': 'AIzaSyA78R_NUhA2hTMv6JYHCe84q9tLKFsoMTQ'}

    response = requests.get(directions, params=param)
    
    json_dict = response.json()

    #Function to Remove HTML tags
    def remove_html(text):
        tag = False   # < >
        quote = False  # " '
        clean_text = ""  # Plain string

        #Itirating through the text to identify special symbols "</'>
        for current in text:
                if current == '<' and not quote:
                    tag = True
                elif current == '>' and not quote:
                    tag = False
                elif (current == '"' or current == "'") and tag:
                    quote = not quote
                elif not tag:
                    clean_text = clean_text + current

        return clean_text

    await bot.say("You have selected the following language: [" + myLanguage + "]   :tongue:  ")
    await bot.say("You have entered [" +  myMode + "] as the method of transportation  :ok_hand:  ")
    await bot.say("Loading directions from [" + userStart + "]  to  [" + userFinish + "] :airplane: ")
    await bot.say("Showing directions...")
    
    for i in range (0, len (json_dict['routes'][0]['legs'][0]['steps'])):
    
    #Repeated Routes, legs, steps printed in HTML format.
            await bot.say(remove_html(json_dict['routes'][0]['legs'][0]['steps'][i]['html_instructions']))
    #Calling the function remove_html to remove HTML TAGS & QUOTES.



    




bot.run('Mjk5NTkwMTE3NzI5NzYzMzMx.C8gGzA.M1gH9w_XI_4iBKA9XsEhnUPm82w')

    
