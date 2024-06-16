friends = ['joya','nayon','sadia','mithi','anik']
p = input('Enter a name: ')
flag = False
for friend in friends:
    if( p == friend):
        print('Your friend is found')
        flag = True
        break

if (flag == False):
    print('Friend is not found')