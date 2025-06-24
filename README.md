## Data Validation Pipeline

### AWS Services Used
* Data Storage - AWS S3 
* Data Transformation - AWS Lambda
* Permissions - IAM
* Deployment - AWS CDK

### Data Pipeline architecture
* Data is uploaded to AWS S3
* The Upload triggers AWS lambda to process data (perform data quality checks)
* Data is loaded back to S3 under a different folder

## Upcoming
* snowflake integration
* load data into snowflake from s3


#### Super FUN!