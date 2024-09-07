# i = 1
# N = 4
# while i <= N:
#     for j in range(1,i+1):
#         print(f"{j}",end="")
#     for k in range(i-1,0,-1):
#         print(f"{k}",end="")
#     i += 1


'''
honestly - easy pattern - just range manipulation and it works easily
'''

def numberPattern(N):
    i = 1
    result = []

    while i <= N:
        string = ''
        for j in range(1,i+1):
            # print(f"{j}",end="")
            string += str(j)
        for k in range(i-1,0,-1):
            string += str(k)
        result.append(string)
        i += 1
    return result

answer = numberPattern(4)
for elem in answer:
    print(elem)