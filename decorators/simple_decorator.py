def decorator_func(func):
    def wrapper():
        print('Функция обертка!')
        print(f'Функция {func}')
        func()
        print('Выход из обертки')
    return wrapper


@decorator_func
def hello_world():
    print('Hello World!')

hello_world()