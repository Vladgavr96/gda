import requests

res = requests.put(url='https://jsonplaceholder.typicode.com/posts/1')
print(res.json()['title'])
#print(res.json()[0:5])