import pyowm

@bot.command()
async def weather(location : str, degree_type : str):
   
    Weather_api_key='373e7a45df1267c605daa192476e9aa3'
##This uses the open weather api to retrieve weather using an api key
    owm = pyowm.OWM(Weather_api_key) 

    CurrentWeather = owm.weather_at_place(location)
    Climate = CurrentWeather.get_weather()
    ##Print out the current weather just so it looks bettter

    if degree_type=='celsius':
        await bot.say("Current weather: ")
        ##ths=is actually gives us the current weather that the user chooses
        await bot.say(Climate.get_temperature('celsius'))

    ##doing the same thing as above just for fahrenheit
    elif degree_type == 'fahrenheit':
        await bot.say("Current weather: ")
        await bot.say(Climate.get_temperature('fahrenheit'))
        
    else:
        await bot.say("Incorrect input. Try entering again")