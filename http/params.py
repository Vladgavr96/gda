import requests

params = {'userId': '2'}
res = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
#https://jsonplaceholder.typicode.com/posts/
print(res.json())

