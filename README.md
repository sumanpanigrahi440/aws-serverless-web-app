# Serverless Web Application on AWS

An end-to-end event-driven serverless web application built using AWS managed services.



Architecture Flow:
1. **Frontend Hosting (Amazon S3):** Static website assets (`index.html`, CSS, Vanilla JS) are hosted directly on an Amazon S3 bucket with static website hosting enabled.
2. **API Layer (Amazon API Gateway):** REST API handles incoming HTTP POST requests from the client.
3. **Compute Layer (AWS Lambda):** Serverless Python function processes the incoming payload.
4. **Data Persistence (Amazon DynamoDB):** Stores form submissions and transaction records.
5. **Asynchronous Messaging (Amazon SQS):** Decouples background processing tasks (notifications, asynchronous worker jobs).


 Tech Stack :
- **Frontend:** HTML5, CSS3, JavaScript
- **Cloud Provider:** Amazon Web Services (AWS)
- **Storage & Hosting:** Amazon S3
- **API Management:** Amazon API Gateway
- **Compute:** AWS Lambda (Python)
- **Database:** Amazon DynamoDB
- **Queueing / Messaging:** Amazon SQS


S3 Static Website Configuration :
- **Public Access**: Uncheck "Block all public access"
- **Bucket Policy**: Refer to `s3-bucket-policy.json` for read permissions.
- **Static Website Hosting**: Enabled (Index document: `index.html`)