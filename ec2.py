import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')  # change region if needed

def create_ec2_instance():
    try:
        response = ec2.run_instances(
            ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 (us-east-1)
            InstanceType='t2.micro',
            KeyName='Linux-Key',  # Replace with your EC2 key pair
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'MySimpleInstance'}]
                }
            ]
        )
