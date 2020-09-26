import boto3
import datetime
import os
from botocore import exceptions


class dynamo_connect():

    def __init__(self, name):
        self.name = name
        self.db_connection = boto3.client(
            'dynamodb',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
            )

    def db_set(self, dictionary):
        try:
            self.db_connection.put_item(TableName=self.name, Item=dictionary)

        except exceptions.ParamValidationError as e:
            print(e)

    def db_get(self, date, country):
        response = self.db_connection.get_item(
            TableName=self.name, Key={
            'country':{'S':country},
            'date':{'S':date}
            }
        )
        return response