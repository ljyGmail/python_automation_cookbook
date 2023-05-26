import requests

url = 'http://www.columbia.edu/~fdc/sample.html'

response = requests.get(url)

print(f'response.status_code: {response.status_code}')

print(f'response.text[:100]: {response.text[:100]}')

print(f'response.request.headers: {response.request.headers}')

print(f'response.headers: {response.headers}')

print(f'response.request: {response.request}')

print(f'response.request.url: {response.request.url}')
