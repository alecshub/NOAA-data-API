from NAPI_datacall import NAPI
import NAPI_plottimeseries

# Enter NOAA National Climatic Data Center Token as a string
token = ''
call = NAPI(token)


# Plot a year of temperature highs and lows for Burlington, VT
# For some reason there's no TMAX data at this station in early 2022 so we'll do 2020 - 2021 instead.
parameters = {
    'locationid':'ZIP:05403',
    'startdate':'2020-02-01',
    'enddate':'2021-02-01',
    'units':'standard',
}
data = call.get_data(**parameters)
NAPI_plottimeseries.plottemp(data)