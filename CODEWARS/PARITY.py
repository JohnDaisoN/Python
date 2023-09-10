def find_outlier(integers):
    sum = integers[0] + integers[1] +integers[2]
    three = integers[0:3]
    flag = 1
    if sum % 2 == 0:
        for int in three:
            if int % 2 != 0:
                flag = 0
                break
                
    else :
        flag = 0
        for int in three:
            if int % 2 == 0:
                flag = 1
                
    if flag == 1:
        for int in integers:
            if int % 2 != 0:
                return int
            
    else :
        for int in integers:
            if int % 2 == 0:
                return int


"""def find_outlier(integers):
    even_count = sum(1 for num in integers if num % 2 == 0)
    odd_count = len(integers) - even_count

    if even_count == 1:
        return next(num for num in integers if num % 2 == 0)
    else:
        return next(num for num in integers if num % 2 != 0)"""
