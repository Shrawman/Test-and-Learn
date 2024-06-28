import time
def count_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end= time.time()
        print(func.__name__+" took "+str((end-start)*1000)+ "mili second")
        return result
    return wrapper

@count_time
def square(num):
    r = []
    for i in num:
        r.append(i*i)
    return r

@count_time
def cube(num):
    r = []
    for i in num:
        r.append(i*i*i)
    return r

arr = range(1,100)
rs = square(arr)
rc= cube(arr)
print("\nResult of Square: ",rs,"\n\n\n","Result of Cube: ",rc)