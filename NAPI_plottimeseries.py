import requests
import json
from NAPI_datacall import NAPI
from datetime import datetime
import matplotlib.pyplot as plt


def plottemp(data):
    """Plot temperature data retrieved from API call made with NAPI_datacall.py"""
    
    # Read through results dictionary retrieved from API call and append data to lists.
    highs, highs_dates, lows, lows_dates = [], [], [], []

    for results_dict in data:
        for key, value in results_dict.items():
            if key == "results":
                for data_dict in value:
                    if data_dict['datatype'] == 'TMAX':
                        highs.append(data_dict['value'])
                        date = datetime.strptime(data_dict['date'], '%Y-%m-%dT%H:%M:%S')
                        highs_dates.append(date)
                    if data_dict['datatype'] == 'TMIN':
                        lows.append(data_dict['value'])
                        date = datetime.strptime(data_dict['date'], '%Y-%m-%dT%H:%M:%S')
                        lows_dates.append(date)


    # Plot data.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs_dates, highs, c='red', alpha=0.5)    
    ax.plot(lows_dates, lows, c='blue', alpha=0.5)
    ax.fill_between(highs_dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    ax.set_title(
        "Daily High and Low Temperatures"
        )
    ax.set_xlabel('',fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylim([-5, 100])

    plt.show()


def plotprecip(data):
    """Plot precipitation data retrieved from API call made with NAPI_datacall.py"""
    
    # Read through results dictionary retrieved from API call and append data to lists.
    precip, dates = [], [],

    for results_dict in data:
        for key, value in results_dict.items():
            if key == "results":
                for data_dict in value:
                    if data_dict['datatype'] == 'PRCP':
                        precip.append(data_dict['value'])
                        date = datetime.strptime(data_dict['date'], '%Y-%m-%dT%H:%M:%S')
                        dates.append(date)

    # Plot data.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, precip, c='red', alpha=0.5)

    # Format plot.
    ax.set_title(
        "Daily Precipitation"
        )
    ax.set_xlabel('',fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Precipitation (inches)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylim([0, 2])

    plt.show()
