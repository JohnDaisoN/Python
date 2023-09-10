#Defining function

def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(4,5)
print(out)
print(add(2,4))

#showing none return type in adder fun

def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(56,14)
print(adder(4,5))

#showing single list argument in a fun

def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = sum([2,3,4])
print(out)

#default argument

def greetings(MSG):
    print(f"Good {MSG}")
    print("Welcome to this function show")

greetings("morning")

# but also doing this way works

def greetings(MSG = "morning"):
    print(f"Good {MSG}")
    print("Welcome to this function show")

greetings()
greetings("night")
