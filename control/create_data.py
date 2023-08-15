import random
for i in range(100):
    with open(f"data/{i}.txt", 'w') as f:
        if i == 87:
            f.write('password = qwerty123')
        else:
            f.write(str(random.randint(1, 1000)))