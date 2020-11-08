import json
from back_end_code import main
import os
import sys
from dotenv import load_dotenv

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(CWD, "package"))
load_dotenv()

def lambda_handler(event, context):
    main()
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function ran scuessfully')
    }

lambda_handler(event=None, context=None)