#!/usr/bin/python
import pyowm
import os

owm = pyowm.OWM(os.environ['OPENWEATHER_API_KEY'])  # You MUST provide a valid API key

observation = owm.weather_at_place(os.environ['CITY_NAME']) # Where
w = observation.get_weather()

print ('source=openweathermap, ' + 'city=\"' + os.environ['CITY_NAME'] + '\", description=\"' + w.get_status() + '\", temp=' + str(w.get_temperature('celsius')['temp']) + ', humidity=' + str(w.get_humidity()))
