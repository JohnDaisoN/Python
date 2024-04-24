import random
l = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
index = 0
for i in range(100):
    sr = random.randint(1,10)
    
    if sr in l:
            print('element founded at position ', (l.index(sr)+1))
            index += l.index(sr)+1

    else:   
            print('Not found')
avg = index / 100
print(avg)