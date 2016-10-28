from WeatherAPIXU import *

test = Weather_APIXU('dc9e7f1f5fa84d4aa80193340162710')
print test.help_apixu_weather()
print 'current\n',test.weather_current(query='19031')
print 'forecast\n',test.weather_forecast(query='19031',days='7')
print 'search\n',test.weather_search(query='auto:ip')
print 'history\n',test.weather_history(query='19031',Date = '2016-10-01')['forecast']['forecastday']

