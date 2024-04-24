from datetime import datetime
import matplotlib.pyplot as plt
x = []
y = []
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))




for n in range(1,30):
 x.append(n)
 start = datetime.now()
 var = fib(n)

 print(var)
 end = datetime.now()


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