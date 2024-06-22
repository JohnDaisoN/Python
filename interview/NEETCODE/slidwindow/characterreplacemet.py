class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}# dict to store count of the right character 
        maxf = 0#var to store current macimum freq

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) # the rth element count is incremeneted by 1 inside dict
            maxf = max(maxf, count[s[r]])# now rth element count is incremented, maxf could be that count or previous maxf itself 

            if (r-l+1) - maxf > k:#important - we check if sliding window length - current maximum frequency is exceeding k or not
                count[s[l]] -= 1#if yes we decrement the left character's count by 1
                l += 1# we got to next element 

        return (r-l+1)# can be done using o(26n) or 0(N)
        
'''
fuckign sliding window to mess with me

here i wont even get 1 mark 

but explanation is pretty decently understandable if u have  5 brains


'''