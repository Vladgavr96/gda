import requests

data = {
    "title": "python test",
}
res = requests.put(url='https://jsonplaceholder.typicode.com/posts/1', data=data) #полное обновление
res2 = requests.patch(url='https://jsonplaceholder.typicode.com/posts/1', data=data) #частичное обновление

print(res.json())
print(res2.json())