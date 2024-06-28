import time
import threading


def square(arr):
    print("Printing Squares: ")
    for i in arr:
        time.sleep(0.2)
        print("Square: ", i*i)

def cube(arr):
    print("Printing Cubes: ")
    for i in arr:
        time.sleep(0.2)
        print("Cube: ", i*i*i)


arr = [2,4,5,6]
t = time.time()
t1= threading.Thread(target=square,args=(arr,))
t2= threading.Thread(target=cube,args=(arr,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Program is executed in" ,time.time()-t)