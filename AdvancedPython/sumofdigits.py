def sumofdigits(m):
    if m <= 9:
        return m
    return (m%10) + sumofdigits(m//10)

print(sumofdigits(1234))