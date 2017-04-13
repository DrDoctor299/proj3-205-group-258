import discord
from discord.ext import commands
import random
import urllib.request
from urllib.request import urlopen
import requests


description = '''/add , /multiply , /divide , /subtract , /roll , /choose , /repeat ,
/joined
                 .'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Bot Adding

## this retrieves one image 
@bot.command()
async def img_ret():
    image_link="https://d13yacurqjgara.cloudfront.net/users/2437/screenshots/1394384/n64_logo.png"
    t=urllib.request.urlretrieve(image_link)
    await bot.say(image_link)

 
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
    
# Bot Subtracting
@bot.command() 
async def subtract(left : int, right : int):
    """Subtracts two numbers together."""
    await bot.say(left - right)
    
    
@bot.command() 
async def multiply(left : int, right : int):
    """Multiplies two numbers together."""
    await bot.say(left * right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def echo(*, message: str):
    """Echoes a message once"""
    await bot.say(message)

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='Stevie')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@bot.command()
async def divide(left : int, right: int):
    await bot.say(left/right)


bot.run('Mjk5NTkwMTE3NzI5NzYzMzMx.C8gGzA.M1gH9w_XI_4iBKA9XsEhnUPm82w')
