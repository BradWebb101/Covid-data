import requests
import json
import time

class api_request():

    def __init__(self): 
        pass

    def execute_request(self, method: str, url: str, headers: dict={}, params: dict ={}) -> dict:
        #API blocks all requests if you go over the 1 second request throttle request, had to use sleep to fix this problem
        response = requests.request(method=method, url=url, headers=headers, params=params)
        if response.status_code == 200:
            time.sleep(2)
            return response
        elif response.status_code == 429:
            time.sleep(60)
        else:
            raise Exception(response.text)





            
            