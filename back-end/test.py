import boto3
from dotenv import load_dotenv
import os

load_dotenv()
db_connection = boto3.client(
            'dynamodb',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
            )

tables = db_connection.list_tables()['TableNames']
if 'Movies' in tables:
    print(True)

else:
    print(False)