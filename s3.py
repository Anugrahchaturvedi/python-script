from http import client
from pydoc import cli
from urllib import response
import boto3
client = boto3.client('s3')
client.delete_bucket(Bucket='ksuhal123456', CreateBucketConfiguration={
                     'LocationConstraint': 'ap-south-1'})
response =client.list_buckets()
print(response)
