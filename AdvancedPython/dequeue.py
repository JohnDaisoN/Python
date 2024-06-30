from collections import deque
dq = deque()
s = []
k = 3




dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)
#reverse first k elements
for i in range(k):
    ele = dq.popleft()
    s.append(ele)

while s:
    dq.append(s.pop())
for i in range(len(dq)-k):
    dq.append(dq.popleft())
print(dq)








