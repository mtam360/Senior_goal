import boto3
import os
from dotenv import load_dotenv
load_dotenv()

bucket_name = os.environ['BUCKET_NAME']
local_directory = 'C:\\\\\\\\\\'
session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=os.environ['AWS_REGION']
)

s3 = session.client('s3')

objects = s3.list_objects(Bucket=bucket_name)['Contents']
 #ignored_objects=["IVC.xlsx"]
for obj in objects:
    key = obj['Key']
  #  if(key not in ignored_objects):
    if 'retail' not in key.lower():
       continue
    local_file_path = os.path.join(local_directory, key)
    
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
    
    s3.download_file(bucket_name, key, local_file_path)
    print(f'Downloaded: {key} to {local_file_path}')
