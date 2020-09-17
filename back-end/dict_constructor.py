import datetime
import json
from database_requests import dynamo_connect

class constructor():

    def __init__(self, raw_dict):
        self.raw_dict = raw_dict
        self.todays_date = datetime.datetime.date(datetime.datetime.now())
        self.previous_confirmed = None
        self.previous_deaths = None
        self.data_for_calc()

    def data_for_calc(self):
        previous_day_dict = dynamo_connect('covid_data').db_get((str(self.todays_date - datetime.timedelta(days=1))), self.raw_dict['country'])
        if previous_day_dict['item']:
            self.previous_confirmed = previous_day_dict['Confirmed']['N']
            self.previous_deaths = previous_day_dict['Deaths']['N']
        else:
            self.previous_confirmed = {'N':0}
            self.previous_deaths = {'N':0}


    def to_date_clean_dict(self):
        output_dict = {}
        output_dict['date'] = {'S':str(self.todays_date)}
        output_dict['country'] = {'S':self.raw_dict['country']}
        output_dict['confirmed'] = {'N':self.raw_dict['confirmed']}
        output_dict['deaths'] = {'N':self.raw_dict['deaths']}
        output_dict['todays_confirmed'] = {'N':int(self.raw_dict['confirmed']) - int(self.previous_confirmed['N'])}
        output_dict['todays_deaths'] = {'N':int(self.raw_dict['deaths']) - int(self.previous_deaths['N'])}
        output_dict['7_Day_per_100000'] = {'N':0}
        
        return json.dumps(output_dict)

    # def to_date_clean_dict(self):
    #     output_dict = {}
    #     output_dict['date'] = {'S':str(self.todays_date)}
    #     output_dict['country'] = {'S':self.raw_dict['country']}
    #     output_dict['confirmed'] = {'N':self.raw_dict['confirmed']}
    #     output_dict['deaths'] = {'N':self.raw_dict['deaths']}
    #     output_dict['todays_confirmed'] = {'N':int(self.raw_dict['confirmed']) - int(self.previous_confirmed['N'])}
    #     output_dict['todays_deaths'] = {'N':int(self.raw_dict['deaths']) - int(self.previous_deaths['N'])}
    #     output_dict['7_Day_per_100000'] = {'N':0}
        
    #     return output_dict

        