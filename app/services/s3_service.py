import boto3, os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

def generate_presigned_url(key: str, expiration=3600):
    return s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": os.getenv("AWS_BUCKET_NAME"), "Key": key},
        ExpiresIn=expiration
    )
