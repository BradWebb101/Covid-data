import datetime
import json
from database_requests import dynamo_connect

class constructor():

    def __init__(self, covid_dict, population_dict):
        self.covid_dict = covid_dict
        self.population_dict = population_dict
        self.todays_date = datetime.datetime.date(datetime.datetime.now())
        self.previous_confirmed = None
        self.previous_deaths = None
        self.data_for_calc()

    def data_for_calc(self):
        try:
            previous_day_dict = dynamo_connect('covid_data').db_get((str(self.todays_date - datetime.timedelta(days=1))), self.covid_dict['country'])
            self.previous_confirmed = previous_day_dict['Item']['confirmed']
            self.previous_deaths = previous_day_dict['Item']['deaths']

        except KeyError: 
            self.previous_confirmed = {'N':str(0)}
            self.previous_deaths = {'N':str(0)}

    def print_dict_values(self):
        print(self.previous_confirmed)
        print(self.previous_deaths)
        
    
    def to_date_clean_dict(self):
        output_dict = {}
        output_dict['date'] = {'S':str(self.todays_date)}
        output_dict['country'] = {'S':self.covid_dict['country']}
        output_dict['confirmed'] = {'N':str(self.covid_dict['confirmed'])}
        output_dict['deaths'] = {'N':str(self.covid_dict['deaths'])}
        output_dict['todays_cases'] = {'N':str(int(self.covid_dict['confirmed']) - int(self.previous_confirmed['N']))}
        output_dict['todays_deaths'] = {'N':str(int(self.covid_dict['deaths']) - int(self.previous_deaths['N']))}
        output_dict['population'] = {'N':str(self.population_dict['population'])}
        output_dict['deaths_per_100k'] = {'N':str((int(output_dict['todays_deaths']['N'])/int(output_dict['population']['N']))*100000)}
        output_dict['cases_per_100k'] = {'N':str((int(output_dict['todays_cases']['N'])/int(output_dict['population']['N']))*100000)}
        output_dict['TTL'] = {'N': str((datetime.datetime.now() + datetime.timedelta(days=8)).timestamp() * 1000)}

        return output_dict
