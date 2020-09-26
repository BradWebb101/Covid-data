from dotenv import load_dotenv
from data_work import data_wrangle
from dict_constructor import constructor
from database_requests import dynamo_connect

if __name__ == '__main__':
    load_dotenv()
    country_list = data_wrangle().get_euro_country_name()
    for i in country_list:
        api_requests = data_wrangle()
        country_data = api_requests.get_covid_data(i)
        population_data = api_requests.get_population(i)
        cleansed_dict = constructor(country_data, population_data).to_date_clean_dict()
        dynamo_connect('covid_data').db_set(cleansed_dict)


