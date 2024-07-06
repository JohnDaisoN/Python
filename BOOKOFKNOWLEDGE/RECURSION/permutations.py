array = [2,3,4,2]

def permutations(array):#this parent function is called on our input array
    def indexed_permurations(l):#this child function is used for taking input always as 0, then
        #recursibely calling itself till all permuations are appended
        if l == len(array)-1:#this is terminating conditon whrn
            #l in some rec call reaches length limit, we get a candidate array - there we append it
            if array.copy() not in s:
                s.append(array.copy())#copy used because we cant modify or do anything with original array
            
            return
        for j in range(l,len(array)):#this range dictates no: of recursive calls

            #first swap done for new element to take or change places like switch places
            array[j],array[l] = array[l],array[j]

            indexed_permurations(l+1)#with switched places array we againc all recurssively 
            array[j],array[l] = array[l],array[j]

            #last switch back because array posiyions must be restored relativewly for 
            #successive transformations to not return a duplicate result 

    s = []
    indexed_permurations(0)
    return s

print(permutations(array))

#notably above solution works only if array has no duplicates

#for future ref - check to remove set instance with result = []

'''
T.C .= = O(n * n!) - o(n) corresponds to array appending or somehting

like operations outside scope of recursivity takes o(n)

for duplicate elements just do a check like if statement as above i guess
'''

    

            