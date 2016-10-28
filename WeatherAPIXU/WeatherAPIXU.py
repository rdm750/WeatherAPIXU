#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

help_txt = \
'''
A simple Library for accessing a https://www.apixu.com/ API. 

REST API Client Lib: GETS JSON data
------------
USAGE:
test = Weather_APIXU('API_KEY')
print test.weather_current(query='19031')
print test.help_apixu_weather()
print 'current ',test.weather_current(query='19031')
print 'forecast ',test.weather_forecast(query='19031',days='7')
print 'search ',test.weather_search(query='auto:ip')
print 'history ',test.weather_history(query='19031',Date = '2016-10-01')['forecast']['forecastday']


Base URL: http://api.apixu.com/v1

-------------

API	API Method
Current weather	/current.json
Forecast	/forecast.json
Search or Autocomplete	/search.json
History	/history.json
Request Parameters

Parameter		Description
key	Required	API Key
q	Required	
Query parameter based on which data is sent back. It could be following:

city name e.g.: q=Paris
US zip e.g.: q=10001
UK postcode e.g: q=SW1
Canada postal code e.g: q=G2J Latitude and Longitude e.g: q=48.8567,2.3508
metar:<metar code> e.g: q=metar:EGLL
iata:<3 digit airport code> e.g: q=iata:DXB
auto:ip IP lookup e.g: q=auto:ip
IP address e.g: q=100.0.0.1
days	Required only with forecast API method.	
Number of days of forecast required.

days parameter value ranges between 1 and 10.e.g: days=5

If no days parameter is provided then only today's weather is returned.

dt	Required only with History API method.	
Date on or after 1st Jan, 2015 in yyyy-MM-dd format (i.e. dt=2015-01-01)

'''

class Weather_APIXU:
	def __init__(self,api_key=None,api_url='http://api.apixu.com/v1/'):
		self.api_key =api_key
		self.api_url = api_url

	def weather_current(self,query=None):
		url = self.api_url + 'current.json?key=' + self.api_key + '&q=' + query 
		#url_current = 'http://api.apixu.com/v1/current.json?key=dc9e7f1f5fa84d4aa80193340162710&q=19031'
		response = requests.get(url).json()
		return response

	def weather_forecast(self,query=None,days=None):
		url = self.api_url + 'forecast.json?key=' + self.api_key + '&q=' + query +',days='+days
		#url_forecast = 'http://api.apixu.com/v1/forecast.json?key=dc9e7f1f5fa84d4aa80193340162710&q=19031,days=7'
		response = requests.get(url).json()
		return response

	def weather_search(self,query=None):
		url = self.api_url + 'search.json?key=' + self.api_key + '&q=' + query
		#url_search = 'http://api.apixu.com/v1/search.json?key=dc9e7f1f5fa84d4aa80193340162710&q=19031'
		response = requests.get(url).json()
		return response

	def weather_history(self,query=None,Date = None):
		url = self.api_url + 'history.json?key=' + self.api_key + '&q=' + query + '&dt=' + Date			
		#url_history = 'http://api.apixu.com/v1/history.json?key=dc9e7f1f5fa84d4aa80193340162710&q=19031&dt=2016-09-01'
		response = requests.get(url).json()
		return response
	def help_apixu_weather(self):
		return help_txt
		

