import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 for printout in pythonins['Instances']:
  for printname in printout['Tags']:
   print(printout['InstanceId'])
   print(printout['InstanceType'])
   print(printout['State']['Name'])
   print(printname['Value'])
   print("=============================== ")