import requests

class ApiClient:

    BASE_URL = "https://fakestoreapi.com"

    def get(self, path:str):
        return requests.get(f"{self.BASE_URL}{path}")
    
    def post(self, path:str, data_json:dict):
        return requests.post(f"{self.BASE_URL}{path}", json=data_json)