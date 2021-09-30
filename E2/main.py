import boto3
client=boto3.client('rds')
response = client.create_db_instance(
    DBName="customerFeedbackDB19",
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='dbinstance19',
    Engine='MySQL',
    MasterUserPassword='pawarayush',
    MasterUsername='root',
    VpcSecurityGroupIds=[
        'sg-08b9cd4a769cff05d',
    ],
    PubliclyAccessible=True,
    AllocatedStorage=5,
)
print(response)