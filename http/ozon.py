import requests

data = {
    "userId": 1,
    "id": 1,
    "title": "python test",
    "body": "text"
}
res = requests.post(url='https://jsonplaceholder.typicode.com/posts', data=data)
print(res.status_code)
print(res.json())
print(type(res.text))
