import requests

response = requests.get("https://fakestoreapi.com/products")
products = response.json()

def return_product_ids():
    return [product['id'] for product in products]

#print(return_product_ids())

def return_all_products():
    return products

#print(return_all_products())