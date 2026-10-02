import os
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    action = event.get('action', 'stop').lower()
    
    # فحص الخوادم المعلمة بـ Tag البيئة
    filters = [
        {
            'Name': 'tag:Environment',
            'Values': ['Development']
        }
    ]
    
    response = ec2.describe_instances(Filters=filters)
    instance_ids = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            
    if not instance_ids:
        return {
            'statusCode': 200,
            'body': 'No matching EC2 instances found with tag Environment=Development.'
        }
        
    if action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        message = f"Successfully stopped instances: {instance_ids}"
    elif action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        message = f"Successfully started instances: {instance_ids}"
    else:
        message = f"Invalid action specified: {action}"
        
    print(message)
    return {
        'statusCode': 200,
        'body': message
    }