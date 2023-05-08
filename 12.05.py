#4
def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"Функція: {func.__name__}, Аргументи: {args}, Результат: {res}")
        return res
    return wrapper
@log
def example_func(x, y):
    return x + y
print(example_func(2, 2))

