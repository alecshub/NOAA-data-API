# NOAA Data API
A user-friendly command-line interface to retrieve, process, and plot NOAA weather data with minimal user input.

## Required packages
- requests
- matplotlib

## Intention
The intention for this project was to develop a user-friendly command-line interface for NOAA's weather data API, which would allow a user to specify a variety of input parameters (e.g., location, start date, end date, type of weather data, units of measurement) and then choose to either receive a plot of those data or download a JSON file. Unfortunately, locating weather stations with good data coverage has been pretty limiting and so instead I've had to settle for providing some example inputs which demonstrate the functionality of the program. Read on to see how it works and try it out for yourself.

## How to aquire NOAA NCEI API token
First you will need to aquire your own unique token in order to make data calls to the NOAA NCEI API. It only takes a minute.
https://www.ncdc.noaa.gov/cdo-web/token

## File process and description
example_file.py is an example user file.

**Instructions**:
1) Enter your unique token as a string at the top of the file. 
2) Uncomment one of the three location options.
3) Uncomment one of the three output options.

Running this file will automatically call functions in the two modules. First it will run the module NAPI_datacall.py. This module will initialize the API call with your unique user token. Then it will run the function get_data. This function will make the API call using the specified example input parameters (locationid, startdate, enddate, and units). Each API call can only return a maximum of 1000 results, so depending on the request, the program will likely need to make several calls. This may take a couple of minutes. You will receive a status code of 200 for every successful call that the program makes. I intentionally have it print out each code so that you know it's working.
