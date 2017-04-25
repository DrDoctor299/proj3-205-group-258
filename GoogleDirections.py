#Google Directions API in Python
#Comments Added by Sergio.

import json, urllib
from urllib import urlencode
import re
import googlemaps
import re

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

#Printing the already decoded URL.
for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    #Repeated Routes, legs, steps printed in HTML format.
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    print j

    
