from data_work import data_wrangle
from dict_constructor import constructor
from database_requests import dynamo_connect

def main():
    country_list = data_wrangle().get_euro_country_name()
    for i in country_list:
        country_covid_data = data_wrangle().get_covid_data(i)
        population_data = data_wrangle().get_population(i)
        cleansed_dict = constructor(country_covid_data, population_data).to_date_clean_dict()
        dynamo_connect('covid_data').db_set(cleansed_dict)



if __name__ == '__main__':
    main()


