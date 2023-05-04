# NOAA Data API
A user-friendly command-line interface to retrieve, process, and plot NOAA weather data with minimal user input.

## Intention
The intention for this project was to develop a user-friendly command-line interface for NOAA's weather data API, which would allow a user to specify a variety of input parameters (e.g., location, start date, end date, type of weather data, units of measurement) and then choose to either receive a plot of those data or download a JSON file. Unfortunately, NOAA weather stations have spotty geographic and temporal coverage so messing with the input parameters often returns no data. In order to demonstrate the functionality of the program, I've had to settle for providing some example inputs. Read on to see how it works and try it out for yourself.

## How to get up and running


1) Install required packages using pip or conda:
- requests
- matplotlib

2) Download all project files from github and save in one folder.

3) Open the example file (example_file.py) in your IDE.

4) Aquire your own unique NOAA API token. It only takes a minute.  
https://www.ncdc.noaa.gov/cdo-web/token

**Instructions**:
1) Enter your unique token as a string at the top of example_file.py. 
2) Uncomment one of the three location options.
3) Uncomment one of the three output options.

Running this file will automatically call functions in the two modules. First it will run the module NAPI_datacall.py. This module will initialize the API call with your unique user token. Then it will run the function get_data. This function will make the API call using the specified example input parameters (locationid, startdate, enddate, and units). Each API call can only return a maximum of 1000 results, so depending on the request, the program will likely need to make several calls. This may take a couple of minutes. You will receive a status code of 200 for every successful call that the program makes. I intentionally have it print out each code so that you know it's working.
