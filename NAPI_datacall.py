import requests
import json


class NAPI:
    """A class that helps users to access the endpoints of the NOAA National Centers for Environmental Information Climate Data Online API."""

    def __init__(self, token):
        """Initialize the API call with a unique user token. Enter token in the file plottemp.py, not here."""
        self.token = token


    def get_data(self, **kwargs):
        """Make API call using kwargs like locationid, startdate, enddate, and units."""
        
        # Set default keyward arguments
        kwargs['datasetid'] = 'GHCND'

        # Loop through the API call until all results are returned. Each call has as max limit of 1000 results.
        limit = 1000
        offset_value = 0

        kwargs['limit'] = limit
        kwargs['offset'] = offset_value

        response_list = []
        while True:
            url = f'https://www.ncei.noaa.gov/cdo-web/api/v2/data'
            headers = {'token': self.token}
            r = requests.get(url, headers=headers, params=kwargs)
            print(f"Status code: {r.status_code}\n")

            response_dict = r.json()
            response_list.append(response_dict)
            

            if len(response_dict['results']) < 1000:
                break
            else:
                offset_value += 1000
                kwargs['limit'] = limit
                kwargs['offset'] = offset_value

        return(response_list)


    def download_data(self, **kwargs):
        """Make API call using kwargs like locationid, startdate, enddate, and units. Then download JSON file."""

        #Set default keyward arguments
        kwargs['datasetid'] = 'GHCND'

        # Loop through the API call until all results are appended to the file. Each call has as max limit of 1000 results. Download JSON file.
        limit = 1000
        offset_value = 0

        kwargs['limit'] = limit
        kwargs['offset'] = offset_value

        while True:
            url = f'https://www.ncei.noaa.gov/cdo-web/api/v2/data'
            headers = {'token': self.token}
            r = requests.get(url, headers=headers, params=kwargs)
            print(f"Status code: {r.status_code}\n")

            response_dict = r.json()
            # data.append(response_dict)
            readable_file = 'data/noaa_data.json'
            with open(readable_file, 'a') as f:
                json.dump(response_dict, f, indent=4)
            

            if len(response_dict['results']) < 1000:
                break
            else:
                offset_value += 1000
                kwargs['limit'] = limit
                kwargs['offset'] = offset_value
