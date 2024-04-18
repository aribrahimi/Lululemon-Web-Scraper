import json
import requests

def lambda_handler(event, context):
    urls = [
        "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
        "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
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