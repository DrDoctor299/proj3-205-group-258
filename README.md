Name of Project: Discord Chat Bot with Commands

Team Members: Sergio Llopis Donate, Joel Casillas, Joshua Williams

Course: CST 205

Date: 5/15/2017

Github Link: https://github.com/DrDoctor299/proj3-205-group-258

For this program, you will need to install the latest version of Python 3 (and will not be able to run from cloud 9): https://www.python.org/downloads/release/python-361/

You will also need an account with Discord (it's free).
You will need to create a new server which you can add your bot to (if you do not have one already)

How to run:
Then you will need to create your own bot and obtain your key: https://discordapp.com/developers/applications/me
For step by step instructions, follow this link:
https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

Once you have your application id, enter this url into any browser:
https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0 
You may select your newly created server, and then add the bot to it.

Go into the Main.py file and change the value of TOKEN (at the top) to be equal to a string of the token generated on the developer page.

Install the following libraries to ensure all of the commands work as intended.

pip install googlemaps

pip install json

pip install request

pip install urllib3 (Important to download version lib3)

pip install urlopen

pip install py_ms_cognifitive

pip install youtube-dl

pip install pyowm

pip install asyncio

pip install -U discord.py[voice]

pip install PyNaCl

pip install aiohttp

You will also need to install the ffmpeg player on your system, and add its /bin folder to your PATH environment variable
Download Link: https://ffmpeg.org/

Future work will include implementing a soundboard. This will stream audio from a file (rather than Youtube).
Future versions will also include event handling (entering and leaving a voice channel)
Future versions will have a more detailed queue function, which will allow users to print the entire queue; and edit individual lines.
Future work will also iron out various bugs discovered in the meantime.



