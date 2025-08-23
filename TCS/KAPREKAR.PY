lower = int(input())
upper = int(input())
flag = -1
for elem in range(lower,upper):
    STRING = str(elem)
    square = elem ** 2
    remaining = 0
    right = int(str(square)[-len(STRING):])
   
    if elem in range(1,4):
        left = 0
    else:
        remaining = len(str(square)) - len(STRING)
        left = int(str(square)[:remaining])
    
    if elem ==  left + right:
        
        print(elem)
        flag = 0
if flag == -1:
    print('INVALID RANGE')