# import boto3
# import json
# import pandas as pd

# dynamodb = boto3.client('dynamodb')
# response = dynamodb.scan(TableName='covid_data')
# master_dict = {}
# for index, item in enumerate(response['Items']):
#     if response['Items'][index]['Country']['S'] == response['Ims'][index-1]['Country']['S']:
#         master_dict[response['Items'][index]['Country']['S']] = {response['Items'][index]['Date']['S']: int(response['Items'][index]['Deaths']['N']) - int(response['Items'][index-1]['Deaths']['N'])}
    
# print(master_dict)    

from database_requests import dynamo_connect

test = dynamo_connect('covid_data').db_get('2020-09-14', 'Austria')

print(test)


# master_list = []
# list_1 = []
# for item in response['Items']:
#     if item['Country']['S'] not in master_list:
#         master_list.append(item['Country']['S'])

# for unique_item in master_list:
#     for item in enumerate(response['Items'], index):
#         if unique_item == item['Country']['S']:
#             list_1.append({'country': unique_item, 'date':item['Date']['S'], 'deaths':item['Deaths']['N']})




# print(df.head())