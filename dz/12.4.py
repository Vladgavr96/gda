f4 = open('test_text.txt', mode='r+', encoding='utf8')
book = f4.read()
book = ' '.join(book.split('\n'))
book = ' '.join(book.split(','))
book = ' '.join(book.split('.'))
list2 = book.split(' ')
c = 0
d = 0
for i in list2:
    if len(i) >= c:
        c = len(i.strip())
        d = list2.index(i)
print(list2[d])
print(f'Количество символов: {c}')
print(len('интернет-энциклопедия'))
f4.close()