from calendar import c
from prettytable import PrettyTable

import boto3
x = PrettyTable()
client = boto3.client('autoscaling', region_name='us-east-1')
all_asg_info = client.describe_auto_scaling_groups()

counter = 0
x.field_names = ["S_no.", "ASG_NAME", "MAX-SIZE",
                 "MIN-SIZE", "CURRENT-DESIRED-VALUE"]
for all_asg in all_asg_info['AutoScalingGroups']:
    counter = counter+1
    x.add_rows(
        [
            [counter, all_asg['AutoScalingGroupName'], all_asg['MaxSize'],
                all_asg['MinSize'], all_asg['DesiredCapacity']],
        ]
    )
print(x)

global_asg_name = ""
count = int(input("Enter S_no. of ASG: "))
counter1 = 0
for all_asg in all_asg_info['AutoScalingGroups']:
    counter1 = counter1+1
    if counter1 == count:
        global_asg_name = all_asg['AutoScalingGroupName']


def update(AutoScalingGroupname, desired_value):
    response = client.update_auto_scaling_group(
        AutoScalingGroupName=AutoScalingGroupname,
        DesiredCapacity=desired_value)


print('SELECTED_ASG: ', global_asg_name)
desired_value = int(input("Enter desired value: "))

update(global_asg_name, desired_value)
