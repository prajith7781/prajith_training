import time

def decorator_timer(function):
    

    def wrapper(p,q):
        t1 = time.time()
        result = function(p,q)
        end = time.time()-t1
        return result, end
    return wrapper


@decorator_timer
def my_pow(p, q):
    res = p ** q
    return res
    

result,exec_time = my_pow(40000, 50000)
print("exec_time:",exec_time ) 
