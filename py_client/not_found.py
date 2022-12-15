import requests

endpoint = "http://localhost:8000/products/38098498139/" 

get_response = requests.get(endpoint) 
print(get_response.json())