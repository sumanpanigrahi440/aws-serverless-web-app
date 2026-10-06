# End-to-End Serverless Web Application on AWS

A fully serverless 3-tier web application built on AWS utilizing static hosting, edge distribution, managed APIs, serverless compute, decoupled queues, and NoSQL storage.

## Architecture
- **DNS & CDN:** Amazon Route 53 & Amazon CloudFront
- **Frontend Hosting:** Amazon S3 (Origin Access Control)
- **Frontend Stack:** Vanilla HTML5, CSS3, JavaScript (Fetch API)
- **API Management:** Amazon API Gateway (HTTP API with CORS)
- **Compute:** AWS Lambda (Python 3.12 / Boto3)
- **Database:** Amazon DynamoDB (NoSQL)
- **Decoupling / Queue:** Amazon SQS (Standard Queue)
- **IAM:** Least-privilege IAM policies for execution roles