from flask import Flask
from flask_restful import Api, Resource
import sqlalchemy as db
import pandas as pd

app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
    def get(self, name):
        pass


api.add_resource(hello_world, '/hello_world/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)