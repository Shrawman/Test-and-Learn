class Accident(Exception):
    def __init__(self, msg) :
        self.message = msg
    
    def print_exception(self):
        print("User defined excption", self.msg)
        
try:
    raise MemoryError('Memory Error')
except MemoryError as e:
    print(e)