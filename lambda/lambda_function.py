import os
import boto3

s3 = boto3.client('s3')
bucket_name  = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    print(event)

    "creating input and output folders within s3"
    s3.put_object(
        BUCKET=bucket_name, 
        Key='input/')
    
    s3.put_object(
        BUCKET=bucket_name, 
        Key='output/')

    return {
        'status code: ': 200,
        'body': "Folders created"
        }