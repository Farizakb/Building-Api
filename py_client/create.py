import requests


headers = {'Authorization': 'Bearer  6c44c0c931a30f44191bdfa3e848a7de2febf6b9'}
endpoint = "http://127.0.0.1:8000/products" 

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())