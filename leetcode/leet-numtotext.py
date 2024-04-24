num = input('Enter a number: ')

d = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: "sixteen", 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}

def convert_to_words(n):
    if n <= 20:
        return d[n]
    elif n < 100:
        tens = d[n // 10 * 10]
        if n % 10 != 0:
            units = d[n % 10]
            return f"{tens}-{units}"
        else:
            return tens
    else:
        hundreds = d[n // 100] + ' hundred'
        if n % 100 != 0:
            return hundreds + ' and ' + convert_to_words(n % 100)
        else:
            return hundreds

def print_words(num):
    num = int(num)
    print(convert_to_words(num))

print_words(num)