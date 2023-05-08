#3
def cache(func):
    dict = {}
    def wrapper(*args, **kwargs):
        if args in dict:
            return dict[args]
        else:
            res = func(*args)
            dict[args] = res
            return res, dict
    return wrapper
@cache
def example_function(x,y):
    return x * y
print(example_function(3,3))