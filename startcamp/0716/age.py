import requests

url = 'https://api.agify.io/?name='
name = 'gilwoong'
req_url = url + name

response = requests.get(req_url).json()

print(response['age'])