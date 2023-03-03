import boto3
import os
from dotenv import load_dotenv
load_dotenv()

ACCES_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_ACCESS_KEY')

AWS_REGION = "us-east-1"
EC2_RESOURSE = boto3.resource("ec2", region_name=AWS_REGION, aws_access_key_id=ACCES_KEY, aws_secret_access_key=SECRET_KEY)

instances = EC2_RESOURSE.instances.all()

for instance in instances:
  print(f"EC2 instance id: {instance.id} state: {instance.state['Name']}")
