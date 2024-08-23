
s = '(x((())))'    
Map = {")": "("}
stack = []
maximum = 0
count = 0

for c in s:
    
        if c not in Map:
            if c == '(':
                stack.append(c)
                count = count + 1
            if c != '(' and count > maximum:
                maximum = count

            continue
        if not stack or stack[-1] != Map[c]:
            maxima = -1
            print(maxima)
            break
        stack.pop()
        count -= 1

if  stack:

    print('-1')
else:
    print(maximum)

