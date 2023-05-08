#1
def retur(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper
@retur
def my_function(x):
    return x * 2
result = my_function(5)
print(result)
