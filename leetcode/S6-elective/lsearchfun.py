import random
def linearsearch(l,sr):

    
    if sr in l:
            print('element founded at position ', (l.index(sr)+1))
            return (l.index(sr)+1)
            

    else:   
            print('Not found')
            
        

l = [1,2,3,4,5]
index = 0 
for i in range(100):
    sr = random.randint(1,5)
    index += linearsearch(l,sr)
print(index/100)
