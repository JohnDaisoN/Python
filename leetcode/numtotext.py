num = input('enter string')
d = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:"sixteen", 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

def two(num):
 if len(num) <= 2:

    if int(num) in d:

        print(d[int(num)], end = ' ')
    else:

        if num[0] != '0':
            n = int(num[0])

            print(d[n*10]+d[int(num[1])], end = ' ')
        else:

            print(d[int(num[1])], end = ' ')

if len(num) == 3:
    print(d[int(num[0])] + ' hundred and', end = ' ' )
    two(num[-2:])
if len(num) == 4:
    print(d[int(num[0])] + ' thousand ' + d[int(num[1])] + ' hundred and', end = ' ' )
    two(num[-2:])
if len(num) == 5:   
    two(num[0:2])
    print(' thousand ' + d[int(num[2])] + ' hundred and', end = ' ' )
    two(num[-2:])
if len(num) == 6:
    print(d[int(num[0])] + ' lakh ', end = ' ' )
    two(num[1:3])
    print(' thousand ' + d[int(num[3])] + ' hundred and', end = ' ' )
    two(num[-2:])
if len(num) == 7:
    two(num[0:2])
    print(' lakh ', end = ' ' )
    two(num[2:4])
    print(' thousand ' + d[int(num[4])] + ' hundred and', end = ' ' )
    two(num[-2:])
    


