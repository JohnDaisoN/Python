
word1 = "Bro"
word2 = "broski"
       
min_len = min(len(word1), len(word2))
merged = []
    
for i in range(min_len):
    merged.append(word1[i])
    merged.append(word2[i])

    # Append the remaining characters from the longer word, if any
if len(word1) > len(word2):
    merged.extend(word1[min_len:])
elif len(word2) > len(word1):
    merged.extend(word2[min_len:])
    
print(''.join(merged))

'''
the function extend can be used to get the extra characters from a certain index
.join(merged) converts the list to a string because we need to return string
'''
    