import boto3
from botocore.exceptions import ClientError
import csv
import os
from country_list import country_api_request
from datetime import datetime
from api_request import api_request
 
class aws_connection():

    def __init__(self):
        pass

    # def get_song(self, artist, song):
        
    #     dynamodb = boto3.client('dynamodb', region_name='eu-west-2')
            
    #     try:
    #         return dynamodb.get_item(TableName='test', Key={'Artist': {'S': artist}, 'SongTitle': {'S':song}})

    #     except ClientError as e:
    #         print(e.response['Error']['Message'])
     
   
    def update_values(self, country_code_list):
        dynamodb = boto3.client('dynamodb', region_name='eu-west-2')
        for country in country_code_list:
            try:
                response = api_request.covid_api_request(country)
                table = dynamodb.Table('covid_data')
                table.put_item(Item=country_data)
            
            except response


if __name__ == "__main__":
    pass