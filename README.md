# WeatherAPIXU
 - - - -
##WeatherAPIXU REST JSON Client Library 
 - - - -
A simple Library for accessing a <https://www.apixu.com>/ API.
```
sudo pip install WeatherAPIXU
```
<https://pypi.python.org/pypi/WeatherAPIXU/0.0.2>


REST API Client Lib: GETS JSON data
 - - - -
```
USAGE:
test = Weather_APIXU('API_KEY')
print test.weather_current(query='19031')
print test.help_apixu_weather()
print 'current ',test.weather_current(query='19031')
print 'forecast ',test.weather_forecast(query='19031',days='7')
print 'search ',test.weather_search(query='auto:ip')
print 'history ',test.weather_history(query='19031',Date = '2016-10-01')['forecast']['forecastday']
```

Base URL: <http://api.apixu.com/v1>

#Steps:

1. Download Folder WeatherAPIXU to local computer except build folder.

    ```
    $ ls -ltr | awk '{print $1,$9}'
    total 
    -rw-r--r--@ setup.py
    drwxr-xr-x WeatherAPIXU
    -rw-r--r--@ examples.py
    ```
    
2. Run setup.py

    ```    
    sudo python setup.py install
    ```
    
3. Check Installation using pip utility

    ```
    $ pip show WeatherAPIXU    
    Metadata-Version: 1.1
    Name: WeatherAPIXU
    Version: 0.0.1
    Summary: Get Weather using API Apixu.com
    Home-page: UNKNOWN
    Author: Rohit Malgaonkar <http://github.com/rdm750>
    Author-email: rdm750@gmail.com
    License: UNKNOWN
    Location: /Library/Python/2.7/site-packages
    Requires: 
    Classifiers:
      Development Status :: 1 - Production/Beta
      Environment :: Web Environment
      Intended Audience :: Developers
      Operating System :: OS Independent
      Topic :: Internet :: WWW/HTTP
      Topic :: Internet :: WWW/HTTP :: Dynamic Content
      Topic :: Software Development :: Libraries :: Application Frameworks
      Topic :: Software Development :: Libraries :: Python Modules
      Intended Audience :: Developers
    ```

4. Run Examples to check if import in Python (tested on 2.7)
    ```
    $ python examples.py

    A simple Library for accessing a https://www.apixu.com/ API. 

    REST API Client Lib: GETS JSON data
    
    USAGE:
    test = Weather_APIXU('API_KEY')
    print test.weather_current(query='19031')
    print test.help_apixu_weather()
    print 'current ',test.weather_current(query='19031')
    print 'forecast ',test.weather_forecast(query='19031',days='7')
    print 'search ',test.weather_search(query='auto:ip')
    print 'history ',test.weather_history(query='19031',Date = '2016-10-01')['forecast']['forecastday']


    Base URL: http://api.apixu.com/v1

    ....
    .......
    .........    
    ```
 - - - -    
####Free to Use .  Request Free API Key from <https://www.apixu.com/>
