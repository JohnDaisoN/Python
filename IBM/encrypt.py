def encrypt_string(s):
    encrypted = []
    count = 1
    
    # Loop through the string to identify repeating characters
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                encrypted.append(f"{s[i - 1]}{count}")
            else:
                encrypted.append(s[i - 1])
            count = 1
    print( encrypted)
    
    return ''.join(encrypted)

# Example usage
input_string = "jdjjdjdhhheld"
encrypted_string = encrypt_string(input_string)
print("Encrypted string:", encrypted_string)
