f = open('test2.txt', mode='a+')#, encoding='cp1251')
print(f)
f.write('\nтест')
#data = f.read()
f.seek(0)
print(f.read())
#print(data)
f.close()
print(f.closed)