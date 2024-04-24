from datetime import datetime
import matplotlib.pyplot as plt
x = []
y = []




def fibnon_rec(n):

    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:

        return b
    else:

        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b



for n in range(1,30):
 x.append(n)
 start = datetime.now()
 var = fibnon_rec(n)
 end = datetime.now()

 print(var)
 td = (end-start).total_seconds() * 10**3
 y.append(td)
 print(f"The execution time is: {td:.03f}ms")

plt.plot(x, y)
plt.xlabel('value')
# naming the y axis
plt.ylabel('time-taken')
 
# giving a title to my graph
plt.title('Non-rec FIBONACCI TIME COMPLEXITY!')
 
# function to show the plot
plt.show()