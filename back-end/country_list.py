import requests
import json
import os

class country_api_request():
   
    def __init__(self):
        pass

    @staticmethod
    def get_country_list() -> dict:
        try:
            euro_countries = {}
            euro_country_list = country_api_request.get_euro_country_list()
            url = 'https://covid-19-data.p.rapidapi.com/help/countries'
            querystring = {"format":"json"}
            headers = {
                'x-rapidapi-host': os.getenv(RAPID_HOST_NAME),
                'x-rapidapi-key': os.getenv(RAPID_HOST_KEY)
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            total_country_list = json.loads(response.text)
            for i in total_country_list:
                if i['name'] in euro_country_list:
                    euro_countries[i['name']] = i['alpha2code']
                #euro_countries[i] = total_country_list[i][alpha2code]
                
            print(euro_countries)

        except Exception as e:
            #Add in error exception
            print(e)

   

    @staticmethod
    def get_euro_country_list() -> list:
        try:
            url = 'https://pkgstore.datahub.io/opendatafortaxjustice/listofeucountries/listofeucountries_json/data/3fb1782af0c2090eb7120573c515d61d/listofeucountries_json.json'
            response = requests.request("GET", url)
            euro_country_dict = json.loads(response.text)
            country_name_list = []
            for i in euro_country_dict:
                for k,v in i.items():
                    if v == 'Slovak Republic':
                        v = 'Slovakia'
                        country_name_list.append(v)
                    elif v == 'United Kingdom':
                        pass
                    else:    
                        country_name_list.append(v)
            
            return country_name_list

        except Exception as e:
            #Add in error exception
            print(repr(e))

        
        

if __name__ == '__main__':
    country_api_request.get_country_list()  

