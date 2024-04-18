# Lululemon Web Scraper API

## Overview
This API provides a simple interface for retrieving product details from Lululemon's web pages. It scrapes product names from the listed URLs and returns them in a JSON format.

## Repository Structure
- `lambda_function.py`: The Python code executed by AWS Lambda to perform web scraping.
- `requirements.txt`: A list of Python packages required for the Lambda function to run.
- `template.yaml`: AWS CloudFormation template for deploying the API and Lambda function.

## Deployment Instructions
To deploy this API, you will need an AWS account. Follow these steps:
1. Create a new Lambda function in the AWS Console.
2. Upload the `lambda_function.zip` file containing the deployment package.
3. Set the Lambda handler to `lambda_function.lambda_handler`.
4. Create a new REST API in API Gateway and link it to your Lambda function.
5. Deploy your API and note the Invoke URL provided by API Gateway.

## API Endpoints
### Retrieve Product Details
- **URL**: `https://ol7vg2h26i.execute-api.us-east-1.amazonaws.com/Dev`
- **HTTP Method**: `GET`
- **Query Parameters**: None
- **Success Response**:
  - **Code**: `200 OK`
  - **Content**:
    ```json
    [
      {"productName": "Wunder Train High-Rise Tight 25\""},
      {"productName": "Classic Unisex Ball Cap *Wordmark"}
    ]
    ```
- **Error Response**:
  - **Code**: `500 Internal Server Error`
  - **Content**: `{"message": "Internal server error"}`

## Testing the API
You can test the API using tools like `curl` or Postman. Example `curl` request:
```bash
curl -X GET https://ol7vg2h26i.execute-api.us-east-1.amazonaws.com/Dev
```

## Caching Strategy

!
To implement caching mechanisms for your API to avoid hitting the Lululemon API excessively, you can use several approaches, especially if you're using AWS services:

### API Gateway Caching:

In API Gateway, you can enable caching on your stage to cache responses from your endpoints. This means that repeated requests with the same parameters will return a cached response rather than invoking the Lambda function again. You can set the TTL (time to live) for the cache to control how long the responses are stored.

### Lambda Function Caching with Elasticache or DAX:

Inside your Lambda function, before making a call to the Lululemon API, you can check if the response to the request is already stored in an AWS ElastiCache Redis cache or DynamoDB Accelerator (DAX) if you are using DynamoDB. This requires setting up ElastiCache or DAX and modifying your Lambda function to query the cache before making the external API call.

### Custom Caching Mechanism:

You can implement a custom caching mechanism using DynamoDB or S3. Store the response from the Lululemon API in a DynamoDB table or an S3 object with a TTL attribute. Before calling the external API, check if the data you need is available and not expired in your cache.

### Using Cloud Front

## Error Handling
The API returns a `500 Internal Server Error` if any errors occur during the scraping process. These errors are logged to CloudWatch for further investigation.

## Security
- The API endpoint is public but can be secured using API Gateway resource policies, API Key, AWS IAM roles and policies, or Lambda authorizers depending on requirements.

## Contact Information
For any queries or issues, please reach out to ar.ibrahimy@gmail.com.