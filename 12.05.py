#2
import time
def time_fuction(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        rezult = func(*args  , **kwargs)
        end_time = time.time()
        print("Час виконання функції:" , round(end_time - start_time , 2))
        return rezult
    return wrapper
@time_fuction
def example_function(x):
    time.sleep(3)
    return x
print(example_function("Hello my love"))
