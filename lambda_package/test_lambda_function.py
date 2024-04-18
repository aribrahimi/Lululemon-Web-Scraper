# test_lambda_function.py
import pytest
from lambda_function import lambda_handler

def test_lambda_handler():
    response = lambda_handler({}, {}) 
    assert response['statusCode'] == 200
    assert 'Hello World' in response['body']

