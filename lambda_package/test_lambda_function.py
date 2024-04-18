# test_lambda_function.py
import json
from lambda_function import lambda_handler

def test_lambda_handler():
    response = lambda_handler({}, {})  
    assert response['statusCode'] == 200
    
    body = json.loads(response['body'])

    assert any(product['productName'] == "Wunder Train High-Rise Tight 25\"" for product in body), "Product name not found in response"
