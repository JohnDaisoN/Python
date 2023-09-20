str1="ABCABC"
str2 = "ABC"

if str1 + str2 != str2 + str1:
            print('')

def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

common_length = gcd(len(str1), len(str2))
print(f"{str1[:common_length]}")