#Creators: Joshua Williams, Sergio Llopis Donate, Joel Casillas
#Github Link: https://github.com/DrDoctor299/proj3-205-group-258
#Date: 5/15/2017

#--------------------------------------------------
#
TOKEN = "YOUR TOKEN HERE"
#
#--------------------------------------------------

#Bot imports
import discord
import asyncio
from discord.ext import commands

#Music class imports
from math import ceil

#Bot Directions API
import json, requests
import urllib3
import googlemaps

#Image Retrieval
import random
import urllib.request
from urllib.request import urlopen
import requests
from py_ms_cognitive import PyMsCognitiveWebSearch

#Open Weather API
import pyowm

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Utilities Class
class Utilities:

    def __init__(self, bot):
        self.bot = bot

    #Removing number of messages.
    @commands.command(pass_context = True, description='Clear the chatroom text by.')
    async def clear(self, context, numberMessages : int):
        """ Clear messages in the chat room."""
        
        counter = 0
        async for current in bot.logs_from(context.message.channel, limit = numberMessages):
            if counter < numberMessages:
                await bot.delete_message(current)
                counter += 1
                    #await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even

    #Retrieving definitions.
    @commands.command(description='This will ask user for an word and it will return links with definitions')
    async def define(self, user_input : str):
        """ Defines a word."""
        
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


    # Bot Adding
    @commands.command()
    async def add(self, left : int, right : int):
        """Adds two numbers together."""
        await bot.say(left + right)
      
    # Bot Subtracting
    @commands.command() 
    async def subtract(self, left : int, right: int):
        """Subtracts two numbers together."""
        await bot.say(left - right)


    # Bot Dividing  
    @commands.command() 
    async def divide(self, left : int, right : int):
        """Divides two numbers together."""
        await bot.say(left / right)
        

    #Math operation powers.
    @commands.command()
    async def tothepower(self, value : int, power : int):
        """Raises to the inputted power."""
        result = 1
        for x in range(0,power):
            result = result * value
        await bot.say(result)


    #Get direction from one location to another 
    @commands.command(description='Directions from a certain starting point to an ending point. You also pass the mode of transportation, whether it is walking, driving, bicycling. Lastly, you select language, such as ES for Spanish, es for English.')
    async def directions(self, userStart : str, userFinish : str, myMode : str, myLanguage):
        """ Get directions from two points."""
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


    #Open Weather API for temperature and location.
    @commands.command(description='This will get the weather of a certain location, depending on what the user enters')
    async def weather(self, location : str, degree_type : str):
        """ Retrieves the current weather."""
       
        Weather_api_key='373e7a45df1267c605daa192476e9aa3'
    ##This uses the open weather api to retrieve weather using an api key
        owm = pyowm.OWM(Weather_api_key) 

        ##Print out the current weather just so it looks bettter

        if degree_type=='celsius':
            CurrentWeather = owm.weather_at_place(location)
            Climate = CurrentWeather.get_weather()
            await bot.say("Current weather: ")
            ##ths=is actually gives us the current weather that the user chooses
            await bot.say(Climate.get_temperature('celsius'))

        ##doing the same thing as above just for fahrenheit
        elif degree_type == 'fahrenheit':
            CurrentWeather = owm.weather_at_place(location)
            Climate = CurrentWeather.get_weather()
            await bot.say("Current weather: ")
            await bot.say(Climate.get_temperature('fahrenheit'))
            
        else:
            await bot.say("Incorrect input. Try entering again")
    
#---------------------------------------------------------------------------------------------------------------------------------------
#Images Class
class Images:

    def __init__(self, bot):
        self.bot = bot

        
    #Getting an image from Bing API.
    @commands.command(description='Gets a image based on a keyword you enter and it will retrieve links containing images')
    async def get_image(self, user_input:str):
        """ Gets an image."""
        
        #storing the user input of the picture they want to get links of
        image_search="picture of" + user_input
        #This will search the internet with image search since it has the user input in it
        word_search = PyMsCognitiveWebSearch('3d2f4008e4f8429fba7dccb98e855743',image_search)
        #This will store the image search into imahe and gives it a limit of 20 possible images
        image = word_search.search(limit=20)
        
       #THe bot will retrieve these kind of like  aprint statement
        await bot.say(image[0].url)
        await bot.say(image[1].url)


#---------------------------------------------------------------------------------------------------
#Music Commands
#Class responsible for tracking neccessary information in songs (the song queue)
class VoiceEntry:
    #Takes in the context of the /play call as a message for the message argument, and the player object for the ytdl player for the specified song
    def __init__(self, message, player):
        #Takes the calling author and sets it equal to requester 
        self.requester = message.author
        #Takes the calling channel instantiantes 
        self.channel = message.channel
        #Takes in the player object and instantiates it
        self.player = player

    #Sets up how each VoiceEntry object will be printed if it is called for print.
    def __str__(self):
        title = '*{0.title}* '
        requester_name = ' requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = title + ' [{0[0]}m {0[1]}s]'.format(divmod(duration, 60)) + requester_name
        return fmt.format(self.player, self.requester)

#Class responsible for running the player and queue backend
class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.default_volume = 0.6
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.votes = set() #set of voter ids (for skipping songs)
        #Starts infinite loop to run the player
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def skip(self):
        self.votes.clear()
        if self.is_playing():
            self.player.stop()
    
    
    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    #Creates read only properties of the VoiceState class
    @property
    def player(self):
        return self.current.player

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    #Creates infinite loop; allows player to play next song as long as the queue (songs) has more elements
    async def audio_player_task(self):
        while True:
            #Clears flag telling it to play next song, and clear all current votes to skip.
            self.play_next_song.clear()
            self.votes.clear()
            
            #Gets next song out of queue (Includes player object, and command message
            self.current = await self.songs.get()
            
            #Prints current song
            await self.bot.send_message(self.current.channel, 'Now playing:\n ' + str(self.current))
            
            #Starts the player playing the next song
            self.current.player.start()
            
            #Blocks thread until the thread running ffmpeg sets flag (lowers resource consumption)
            await self.play_next_song.wait()
            

#Class contains commands for users
class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_state = None

    def get_voice_state(self):
        state = self.voice_state
        if state is None:
            
            state = VoiceState(self.bot)
            print("instanced new VoiceState")
            self.voice_state = state
            
        return state
            

    #Joins specified voice channel, and sets the voice object to the VoiceState
    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice



    #Summons the bot to the calling user's voice channel
    #Triggers on /play only when the bot is not in a voice channel
    @commands.command(pass_context = True, no_pm = True, description = 'Summons the bot to your current voice channel. Must be in a voice channel to use.')
    async def summon(self, ctx):
        """Summon bot to your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        #Checks if the calling user is in a voice channel
        if summoned_channel is None:
            await self.bot.say('You are not in a voice channel.')
            return False
        #If the bot is not in a voice channel, joins with join_voice_channel
        state = self.get_voice_state()
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        #If the bot is in a voice channel, moves to the summoned_channel with move_to
        else:
            await state.voice.move_to(summoned_channel)

        return True
    #Skips the current song if the requester of the song calls it
    #Calls a vote if someone else calls it, vote_thres or number of people in vc is the required number of votes
    @commands.command(pass_context = True, no_pm = True, description = 'Skips currently playing song. The requester of the song can skip with no vote. Others who use skip will trigger a vote to skip the song (Majority of Voice Channel users rounded up needed to skip). Users must be in Bots voice channel to skip.')
    async def skip(self, ctx):
        """Skip the current song."""

        state = self.get_voice_state()
        other_members = len(state.voice.channel.voice_members) - 1
        neccessary_votes = ceil(other_members/2)
        
        author = ctx.message.author
        
        if not state.is_playing():
            self.bot.say('Nothing is playing at the moment.')
            return

        #Voter must be in same voice channel as bot to vote
        if author.voice.voice_channel == state.voice.channel:
            #If voter is original requester, song skips
            if state.current.requester == author:
                player = state.player
                player.stop()
                
            #If voter has not voted already, adds vote
            elif author is not state.votes:
                #Adds author's id to set, then counts the number of votes
                state.votes.add(author.id)
                await self.bot.say(author.name + ' votes to skip this song!')
                total_votes = len(state.votes)
                #Checks if there are enough votes to skip, if there are, skips, if not, display's progress
                if total_votes >= neccessary_votes:
                    await self.bot.say('The Skips have it! Skipping song.')
                    state.skip()
                else:
                    await self.bot.say(str(total_votes) + '/' + str(neccessary_votes) + ' votes to skip.')
                    
            #If voter has already voted, tells them so
            else:
                await self.bot.say('You have already voted ' + author.nick + '!')
                
        #Tells voter they must be in the same voice channel to skip
        else:
            await self.bot.say('You must be in the same voice channel as me to skip ' + author.nick + '!')

    #Pauses the current stream
    @commands.command(no_pm = True, description = 'Pauses the currently playing song')
    async def pause(self):
        """Pause the current song."""
        
        state = self.get_voice_state()

        #Checks if the bot is connected to a voice channel, or has a current song. 
        if state.is_playing():
            player = state.player
            player.pause()
            
    #Resumes the current stream
    @commands.command(no_pm = True, description = 'Resumes the currently playing song')
    async def resume(self):
        """Resume the current song."""
        
        state = self.get_voice_state()

        #Checks if the bot is connected to a voice channel, or has a current song.
        if state.is_playing():
            player = state.player
            player.resume()

    #Stops the player, cancels the looping task, and disconnects the bot from the voice chat.
    #Also removes the queue
    @commands.command(pass_context=True, no_pm=True, description = 'Stops the music, clears the queue, and disconnects bot from voice channel')
    async def stop(self, ctx):
        """Clear queue and stop the music."""
        
        state = self.get_voice_state()

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            print("inside try/catch")
            state.audio_player.cancel()
            self.voice_state = None
            await state.voice.disconnect()
        except:
            pass
        

    @commands.command(pass_context = True, no_pm = True, description = 'Searches for and plays a song through a keyword, if a song is already playing, queues the song to play next')
    async def play(self, ctx, *, song : str):
        """Play a song through a voice channel."""

        state = self.get_voice_state()
        #Options for the ytdl function
        #default_search makes the function treat the argument as a search term (or URL, whichever is closer)
        opts = {
            'default_search' : 'auto'
        }

        #if bot is not in a voice channel, summon the bot to the calling user's voice channel
        if state.voice is None:
            success = await ctx.invoke(self.summon)
            if not success:
                return

        #Attempts to create a player object for the song search term
        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options = opts, after = state.toggle_next)
        #Handles exceptions
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        #Executes when the player is created successfully
        else:
            #Adjusts volume to default (initialized to 0.6)
            player.volume = state.default_volume
            #Creates VoiceEntry instance as entry
            entry = VoiceEntry(ctx.message, player)
            #Add entry to songs (queue)
            await self.bot.say(str(entry))
            await state.songs.put(entry)


description = '''The MemeTron Super Bot has endless functionality to fight back your crippling depression, annoy your friends, listen to music and pull images.'''
bot = commands.Bot(command_prefix='/', description=description)
bot.add_cog(Utilities(bot))
bot.add_cog(Music(bot))
bot.add_cog(Images(bot))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
