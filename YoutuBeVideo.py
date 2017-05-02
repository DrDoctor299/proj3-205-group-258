import pafy

video = pafy.new('https://www.youtube.com/watch?v=o_M8BgCNh8E')
bestaudio = video.getbestaudio()
bestaudio.bitrate #get bit rate
bestaudio.extension #extension of audio fileurl

print(bestaudio.url) #get url

#download if you want
bestaudio.download()


















# import discord
# from discord.ext import commands
# import random
# import asyncio

# description = '''/add , /multiply , /divide , /subtract , /roll , /choose , /repeat ,
# /joined
#                  .'''
# bot = commands.Bot(command_prefix='/', description=description)

# @bot.command()
# def add(left : int, right : int):
#     """Adds two numbers together."""
#     yield from bot.say(left + right)


# bot.run('token')