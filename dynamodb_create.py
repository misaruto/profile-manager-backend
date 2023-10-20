
import boto3

dynamodb = boto3.resource('dynamodb',region='sa-east-1')

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
          'dynamodb' 
    )

    table = dynamodb.create_table(
        TableName='profile',
        BillingMode="PAY_PER_REQUEST",
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'profileName',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'profileName',
                'AttributeType': 'S'
            },
        ]
    )
    return table

import boto3


def delete_dax_table(dyn_resource=None):
    """
    Deletes the demonstration table.

    :param dyn_resource: Either a Boto3 or DAX resource.
    """
    if dyn_resource is None:
        dyn_resource = boto3.resource('dynamodb')

    table = dyn_resource.Table('profile')
    table.delete()

    print(f"Deleting {table.name}...")
    table.wait_until_not_exists()


if __name__ == '__main__':
    #delete_dax_table(dynamodb)
    users_table = create_table(dynamodb)
    print("Table status:", users_table.table_status)

