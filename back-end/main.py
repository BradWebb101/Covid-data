from flask import Flask 
from flask_restful import Api, Resource
import sqlalchemy as db
import boto3
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
api = Api(app)


class all_data(Resource):
    def get(self):
        dynamodb = boto3.client('dynamodb', 
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION'))
        response = dynamodb.scan(TableName='covid_data')
        return response['Items']

api.add_resource(all_data, '/all_data')

class today(Resource):
    def get(self, country):
        dynamodb = boto3.client('dynamodb', 
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION'))
        response = dynamodb.get_item(
        TableName='covid_data',
        Key={
            'date': {'S':str(datetime.datetime.date(datetime.datetime.now()))},
            'country': {'S':str(country)}
        },
        AttributesToGet = ['country', 'date', 'todays_cases', 
                            'todays_death', 'confirmed', 'deaths', 
                            'cases_per_100k', 'deaths_per_100k']
    )
        return response['Item']

api.add_resource(today, '/today/<country>')

class unique_countries(Resource):
    def get(self):
        dynamodb = boto3.client('dynamodb', 
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION'))
        response = dynamodb.scan(
                        TableName='covid_data',
                        AttributesToGet=['country']
                        )
        unique_countries_list = []
        for item in response['Items']:
            if not item['country']['S'] in unique_countries_list:
                unique_countries_list.append(item['country']['S'])
            else:
                pass
        return unique_countries_list

api.add_resource(unique_countries, '/unique_countries')

if __name__ == '__main__':
    app.run(debug=True)