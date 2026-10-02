import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    filters = [
        {
            'Name': 'tag:Environment',
            'Values': ['Development']
        }
    ]
    
    response = ec2.describe_instances(Filters=filters)
    snapshots_created = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            for volume in instance.get('BlockDeviceMappings', []):
                volume_id = volume['EBS']['VolumeId']
                description = f"Automated snapshot for {instance_id} ({volume_id})"
                
                snapshot = ec2.create_snapshot(
                    VolumeId=volume_id,
                    Description=description,
                    TagSpecifications=[
                        {
                            'ResourceType': 'snapshot',
                            'Tags': [
                                {'Key': 'CreatedBy', 'Value': 'LambdaAutomation'},
                                {'Key': 'InstanceId', 'Value': instance_id}
                            ]
                        }
                    ]
                )
                snapshots_created.append(snapshot['SnapshotId'])
                
    return {
        'statusCode': 200,
        'body': f"Snapshots created: {snapshots_created}"
    }