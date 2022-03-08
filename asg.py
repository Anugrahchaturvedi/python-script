from http import client
import boto3
client = boto3.client('autoscaling')
response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        'my-asg',
    ]
)
response = client.attach_instances(
    InstanceIds=[
        'string',
    ],
    AutoScalingGroupName='string'
)