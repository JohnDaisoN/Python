length = int(input())
rot = int(input())
l = list(map(int,input().split(' ')))
m = [-1 for _ in range(length)]
for i in range(length):
   m[(i-rot) % length] = l[i]
for elem in m:
    print(elem,end=" ")
