import csv

users = [
    ['username', 'password', 'is_admin'],
    ['admin', 'qwerty123', True],
    ['test_user', 'test_password', False]
]

with open('users.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(users)
    writer.writerow(['test_user2', 'test_password2', False])

with open('users.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row)