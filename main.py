import discord
import asyncio
from discord.ext import commands

description = '''    '''
bot = commands.Bot(command_prefix='/', description=description)

TOKEN = "Your_token_here"

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

bot.run(TOKEN)
