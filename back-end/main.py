from flask import Flask 
from flask_restful import Api, Resource
import sqlalchemy as db
import boto3

app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
    def get(self):
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.scan(TableName='covid_data')
        return response['Items']

api.add_resource(hello_world, '/')

if __name__ == '__main__':
    app.run(debug=True)