nums = input('Enter string')
n = []
for elem in nums:
     n.append(elem)

#b = input('Enter second number')
#c = input('Enter third number')
#d = input('Enter four number')
#e = input('Enter fifth number')
#string = str(a+b+c+d)


#new = ""
#i = 0
#def permut(string, new):
    
    #for item in string:
        
        #new += item
       # stri = string.replace(item, "")
        
        #permut(stri, new)
        
#def per(string):       
 #for item in string:
   # a = item
    #string = string.replace(item,"")

def permute(numbers, start=0):
    if start == len(numbers) - 1:
        n = ''.join(numbers)
        print(n)
    else:
        for i in range(start, len(numbers)):
            
            numbers[start], numbers[i] = numbers[i], numbers[start]
            
            
            permute(numbers, start + 1)
            
            
            numbers[start], numbers[i] = numbers[i], numbers[start]


permute(n, start=0)




    

