import requests


endpoints = 'http://127.0.0.1:8000/'


get_response = requests.get(endpoints, json={'salam':'salamm'})
print(get_response.content)