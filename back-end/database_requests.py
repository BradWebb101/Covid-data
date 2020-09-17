import boto3
import datetime


class dynamo_connect():

    def __init__(self, name):
        self.name = name
        self.db_connection = boto3.client('dynamodb')
        

    def db_set(self, dictionary):
        try:
            self.db_connection.put_item(TableName=self.name, Item=dictionary)
        except 

    def db_get(self, date, country):
        try:
            response = self.db_connection.get_item(TableName=self.name, Key={
            'country':{'S':country},
            'date':{'S':date}
                }
            )
            return response['Item']

        except Exception as e:
            print(e)

