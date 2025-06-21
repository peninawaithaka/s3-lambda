from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_s3_notifications as s3n,
    aws_iam as iam,
    RemovalPolicy
)
from constructs import Construct

class S3LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #creating S3 bucket
        bucket = s3.Bucket(
            self, "data-validation",
            bucket_name='data-validation-4545',
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True #deletes the objects too once s3 bucket is deleted
        )

        #creating the lambda function
        s3_lambda = lambda_.Function(
            self, "data-validation-function",
            function_name='data-validation-function',
            handler='lambda_function.lambda_handler',
            runtime=lambda_.Runtime.PYTHON_3_10,
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }
        )

        #connecting s3 to lambda
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(s3_lambda)
        )

        #granting s3-lambda read access to s3
        bucket.grant_read_write(s3_lambda)

