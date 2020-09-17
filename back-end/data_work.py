from request import api_request
import json
import os
import requests

class data_wrangle():

    def __init__(self):
        pass

    def get_euro_country_name(self):
        response = api_request().execute_request(
                            method='GET',
                            url='https://pkgstore.datahub.io/opendatafortaxjustice/listofeucountries/listofeucountries_json/data/3fb1782af0c2090eb7120573c515d61d/listofeucountries_json.json'
                            ) 
        euro_country_dict = json.loads(response.text)
        country_name_list = []
        for i in euro_country_dict:
            for k,v in i.items():
                if v == 'Slovak Republic':
                    country_name_list.append('Slovakia')
                elif v == 'United Kingdom':
                    pass
                else:    
                    country_name_list.append(v)
            
        return country_name_list

    def get_covid_data(self, country: str) -> list:
            try:
                url = "https://covid-19-data.p.rapidapi.com/country"
                querystring = {'format':'json','name':f'{country}'}
                headers={
                        'x-rapidapi-host': os.getenv('RAPID_HOST_NAME'),
                        'x-rapidapi-key': os.getenv('RAPID_HOST_KEY')
                        }
                response = api_request().execute_request(method='GET', url=url, params=querystring, headers=headers)
                return json.loads(response.text)
                
            except requests.exceptions.RequestException as e:
                print(e)
                
