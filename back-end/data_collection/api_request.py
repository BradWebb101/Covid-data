
import datetime as dt
import json
import requests
import country_list


class api_request():

    def __init__(self):
        pass

    def covid_api_request(self, country_code):
        try:
            url = f"https://api.covid19api.com/live/country/{country_code['x']}/status/confirmed/date/{dt.datetime.today().isoformat() + 'Z'}"
            print(url)
            payload = {}
            headers= {}

            response = requests.request("GET", url, headers=headers, data = payload)
            if response.status_code == requests.codes.ok:
                return json.loads(response.text)
            else:
                return (f'The following error occurered {response.status_code}')

        except requests.exceptions.HTTPError as e:
            return "An Http Error occurred:" + repr(e)
        except requests.exceptions.ConnectionError as e:
            return "An Error Connecting to the API occurred:" + repr(e)
        except requests.exceptions.Timeout as e:
            return "A Timeout Error occurred:" + repr(e)
        except requests.exceptions.RequestException as e:
            return "An Unknown Error occurred" + repr(e)

    # def request_data_test(self):
    #     try:
    #         country_list = country_api_request.get_euro_country_list()
    #         for country_code in country_list:
    #             country_covid_data = self.covid_api_request(country_code)
    #             print(country_covid_data)
    #     except Exception as e:
            print('Error code ' + repr(e))




