from NAPI_datacall import NAPI
import NAPI_plottimeseries

# Enter NOAA National Climatic Data Center Token as a string.
token = ''
call = NAPI(token)


# Uncomment one of the three example option locations below:

# Option 1: Burlington, Vermont
# parameters = {
#     'locationid':'ZIP:05403',
#     'startdate':'2020-02-01',
#     'enddate':'2021-02-01',
#     'units':'standard',
# }

# Option 2: Santa Fe, New Mexico
# parameters = {
#     'locationid':'ZIP:87501',
#     'startdate':'2020-02-01',
#     'enddate':'2021-02-01',
#     'units':'standard',
# }

# Option 3: New York, New York
parameters = {
    'locationid':'ZIP:10023',
    'startdate':'2020-02-01',
    'enddate':'2021-02-01',
    'units':'standard',
}


#Uncomment one of the three output options below:

# Option 1: Make data call and plot temperature data.
data = call.get_data(**parameters)
NAPI_plottimeseries.plottemp(data)

# Option 2: Make data call and plot precipitation data.
# data = call.get_data(**parameters)
# NAPI_plottimeseries.plotprecip(data)

# Option 3: Make data call and download the dataset as .json file. File will download to same folder that the program files are kept.
# data = call.download_data(**parameters)