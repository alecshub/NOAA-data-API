# NAPI
A set of modules that help users to access and plot data from the NOAA National Centers for Environmental Information (NCEI) Climate Data Online API using Python.

### Prerequisite packages
- requests
- json
- datetime
- matplotlib

### How to aquire NOAA NCEI API token
First you will need to aquire your own unique token in order to make data calls to the NOAA NCEI API. It only takes a minute.
https://www.ncdc.noaa.gov/cdo-web/token

### File process and description
plottemp.py is an example user file. Enter your unique token as a string. Running this file will automatically call functions in the two modules. First it will run the module NAPI_datacall.py. This module will initialize the API call with your unique user token. Then it will run the function get_data. This function will make the API call using input parameters like locationid, startdate, enddate, and units, which can be specified in the plottemp.py file. Each API call can only return a max of 1000 results, so depending on the request, the program will likely need to make several calls. This may take a couple of minutes. You will receive a status code of 200 for every successful call that the program makes. It will intentionally print out each code so that you know it is working. Once all of the results have been retrieved, plottemp.py will authomatically run the plottemp function from the NAPI_Plottimeseries.py module. A figure window will open, showing a yealong timeseries of high and low temperatures for Burlington, VT.

### Other functionalities
The intention for this project was to allow a user to specify all information in the input parameters in the file plottemp.py e.g., locationid, startdate, enddate, and units. However, the NOAA NCEI API is clunky and often returns no data for certain time periods and many zipcodes. Exploring https://www.ncdc.noaa.gov/cdo-web/search can help to figure out what zipcodes and time periods there are data for.

NAPI_datacall.py has another function option, download_data, instead using get_data. download_data will download the JSON file of data for later use while get_data stores the data in memory for the time being.

NAPI_plottimeseries has another function option, plotprecip, instead of the function plottemp. plotprecip plots precip data from the location instead of temperature highs and lows.
