friends = ['joya','nayon','sadia','mithi','anik','ashraful']
p = input('Enter a name: ')
flag = False
for friend in friends:
    if( p == friend):
        print('Your friend is found')
        flag = True
        break

if (flag == False):
    sports= ["football","cricket","hockey","basketball"]
    for i in sports:
        print(i)