
import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': 'hello my old friend',
    'price': 129.99
}
get_response = requests.put(endpoint, json=data)  # HTTP request
print(get_response.json())
