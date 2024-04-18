# test_lambda_function.py
import pytest
import requests_mock
from lambda_function import lambda_handler

# Mocking the web pages' content that your Lambda function will scrape
example_leggings_page = {
    "contents": [
        {"mainContent": [
            {"contents": [
                {"records": [
                    {"attributes": {"product.displayName": "Leggings Example Name"}}
                ]}
            ]}
        ]}
    ]
}

example_accessories_page = {
    "contents": [
        {"mainContent": [
            {"contents": [
                {"records": [
                    {"attributes": {"product.displayName": "Accessories Example Name"}}
                ]}
            ]}
        ]}
    ]
}

@pytest.fixture()
def context():
    """Create a mock context object to pass to the lambda_handler."""
    class TestContext:
        def __init__(self):
            self.function_name = 'test_lambda_function'
            self.memory_limit_in_mb = 128
            self.invoked_function_arn = 'arn:aws:lambda:us-east-1:123456789012:function:test_lambda_function'
            self.aws_request_id = 'unique-test-id'

    return TestContext()


@requests_mock.Mocker()
def test_lambda_function_success(m, context):
    # Set up request mocks
    m.get("https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json", json=example_leggings_page)
    m.get("https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json", json=example_accessories_page)

    # Call the lambda_handler function
    response = lambda_handler({}, context)

    # Assert the response is as expected
    assert response['statusCode'] == 200
    assert 'Leggings Example Name' in response['body']
    assert 'Accessories Example Name' in response['body']


@requests_mock.Mocker()
def test_lambda_function_error(m, context):
    # Set up a request mock to return an error
    m.get("https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json", status_code=500)

    # Call the lambda_handler function
    response = lambda_handler({}, context)

    # Assert the function handled the error as expected
    assert response['statusCode'] == 500
    assert "Internal server error" in response['body']
