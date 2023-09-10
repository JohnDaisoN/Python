def narcissistic( value ):
    a = str(value)
    l = len(a)
    new_str = sum((int(item) ** l) for item in a)
    return (int(new_str) == int(a))