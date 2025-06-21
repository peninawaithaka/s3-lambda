#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_lambda.s3_lambda_stack import S3LambdaStack


app = cdk.App()
S3LambdaStack(app, "S3LambdaStack")

app.synth()
