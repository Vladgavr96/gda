import os

os.chdir('data')
for i in os.listdir():
    with open(i) as f:
        data = f.read()
        if 'password' in data:
            print(i)
            print(data)
            break