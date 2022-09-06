def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')

    return wrap_func


@my_decorator
def hello(greeting):
    print(f'Hi!!... {greeting}')


hello('Rupali')

a = my_decorator(hello('Sharma'))


