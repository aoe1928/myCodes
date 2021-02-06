def handler(func, *args):
    return func(*args)


def say_hello(name):
    print('hello')
    print(name)


if __name__ == '__main__':
    callback = say_hello
    handler(callback, 'moroku0519')
