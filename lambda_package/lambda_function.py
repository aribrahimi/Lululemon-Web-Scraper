import json
import requests
import os

def lambda_handler(event, context):
    womens_leggings_url = os.environ.get('WOMENS_LEGGINGS_URL')
    accessories_url = os.environ.get('ACCESSORIES_URL')
    
    urls = [
        womens_leggings_url,
        accessories_url
    ]
    products = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        product_name = data['contents'][0]['mainContent'][0]['contents'][0]['records'][0]['attributes']['product.displayName']
        products.append({'productName': product_name})
        
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(products)
    }