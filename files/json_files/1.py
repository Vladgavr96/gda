import json


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        raise TypeError(f'Object of type {o.__class__.__name__} '
                        f'is not JSON serializable')
# json.encoder
message = {
    'from': 'vlad',
    'to': 'anton',
    'text': 'Hi!',
    'on_delte': None,
    'tuple': (1, 2, 3),
    'number': 5,
    'bool': True,
    #'sets': {1,2,3}
}

json_str = json.dumps(message, cls=MyEncoder)
#print(json_str)
decoded = json.loads(json_str)
#print(decoded)

#with open('message.json', 'w') as f:
#    json.dump(message, f, indent=4)

with open('message.json') as f:
    data = json.load(f)
    print(data)