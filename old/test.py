'''def test():
    print('recursion')
    test()

test()'''


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


def make_a_dict(phone, **kwargs): # name, email, comment
    pass

make_a_dict(phone='88005553535')
result = {
    'phone': '88005553535',
    #'name': 'admin',
    #'comment': 'smth'
}