import random

n = 'yes'
l = [1,2,3,4,5,6]

while n == 'yes':
    random.shuffle(l)
    print(l[0])
    print('Answer Yes or No ')
    n = str(input('Again? '))
    
    
