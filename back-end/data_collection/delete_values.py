import boto3 

class delete_tables():

    def __init__(self):
        self.client = boto3.client('dynamodb')


    def get_table_keys(self):
        response = self.client.scan(TableName='covid_data')
        for item in response['Items']:
            if item['date']['S'] != '2020-11-09':
                print(f'Deleting data')
                self.client.delete_item(TableName='covid_data',
                    Key = {
                        'country':item['country'],
                        'date':item['date']
                    }
                )

if __name__ == '__main__':
    print(delete_tables().get_table_keys())

