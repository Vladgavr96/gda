'''with open('poem.txt') as f:
    file_lines = f.readlines()
    print(file_lines)
    for line in file_lines:
        print(line.strip())

print(f.closed)'''
with open('numbers.txt') as f:
    list1 = f.read().split(',')
    print(list1)
    list1 = list(map(int, list1))
    print(sum(list1))

f = open('numbers.txt')
sum = 0
for i in f:
  sum += int(i)
print(sum)