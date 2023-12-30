from aws_cdk import (
    # Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3
)
from constructs import Construct

class CvStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        bucket = s3.Bucket(self, "example-bucket---filip",
                           access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
                           encryption=s3.BucketEncryption.S3_MANAGED,
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
