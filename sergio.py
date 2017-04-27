#Google Directions API in Python
#Comments Added by Sergio.

import json, urllib
from urllib import urlencode
import googlemaps

# Asking the User for Input for Start and Final Destination.
userStart = raw_input("Please enter your start destination:  ")
userFinish = raw_input("Please enter your final destination:  ")

# Opening the API website using json and encoding it.
url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
           #Parameters for beginning and final destinations.
            ('origin', userStart),
            ('destination', userFinish)
 ))
 
#Using the URLlib module to open up the URL: Maps.Googleapis.com.
ur = urllib.urlopen(url)

#Parsing and decoding the URL.
#Using JavaScript Object Notation (json).
result = json.load(ur)

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
#Returning the actual plain text
    return clean_text
    

#Printing the already decoded URL.
for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    
    #Repeated Routes, legs, steps printed in HTML format.
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    #Calling the function remove_html to remove HTML TAGS & QUOTES.
    print remove_html(j)

    
