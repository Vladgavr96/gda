file = 'фффф.txt'
try:
    with open(file) as f:
        print(f.read())
except:
    with open(file, 'w') as f:
        f.write('Пусто')