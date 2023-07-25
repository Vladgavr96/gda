def hello_world():
    print('Hello World!')

def high_func(func):
    print(f'получена функция {func} в качестве аргумента')
    func()

high_func(hello_world)