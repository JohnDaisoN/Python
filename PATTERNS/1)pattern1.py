'''
You are given a number n. You need to print the pattern for the given value of n.

For n = 2 the pattern will be 
2 2 1 1
2 1

For n = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Note: Instead of printing a new line print a "$" without quotes. After printing the total output, end of the line("$") is expected.
'''
'altogether pretty intuitive - i think you can even use dictionary to store these pattern logic values'

#my code
def printPat(n):
    elemcount = n#i thought i needed a variable to store the initial value to printed at every line - but not manipulate n 
    count = n#count suggests the no_ times each number need to printed - first line n times, then n-1 times.....
    for i in range(n):#no of lines will be n
        # j = 1
        elemcount = n
        
        while elemcount >= 1:#elemcount indicates the element to be printed  - first it will be always be 3 if n = 3
            
            j = 1#j indicates the no:of times 3 is to be printed 
            while j <= count:#first print 3 3 times, 
                print(elemcount,end=" ")
                j += 1
            
            elemcount -= 1#now we need to print 2 - so elemcoiunt decremented and repeat iteration count times 
        print('$',end="")#code req - insteas of newline using $ character
        count -= 1#count decrement after printing all elements from n to 1, 

#i believe this code is apt for understanding

