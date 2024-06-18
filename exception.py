class Accident(Exception):
    def __init__(self, msg) :
        self.message = msg
    
    def print_exception(self):
        print("User defined excption", self.msg)

try:
    x = 1/0
    raise Accident('Crash between two cars')
except Accident as e: 
    print(e) 
finally:   #Even if execptin occured,finally will still execute code
    print("Code executed")