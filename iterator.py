#  s = ["hello", "my", "friend","how","are","you"]
# itr = iter(s)
# revitr= reversed(s)
# print(next(itr))
# print(next(revitr))  # cntrl + /

#Remote Control

# class RemoteControl:
#     def __init__(self):
#         self.channel = ["HBO","Disney","Star Sports","Ten Sports"]
#         self.index = -1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.channel):
#             raise StopIteration
#         return self.channel[self.index]

# r = RemoteControl()
# itr = iter(r)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

def remote_control():
    yield "cnn"
    yield "espn"

x = remote_control()
print(next(x))
print(next(x))