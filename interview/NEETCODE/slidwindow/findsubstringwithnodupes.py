class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    
'''
fuckign i hate sliding window

onlly thing i can actully grasp is that we need a set - because to avoid duplicate characters

we add elements to a set as we see them

we see a duplicate element, then we remove the set elements until we encounter the dupe inside the set

here l - left = is start of array = 0

right is in a for loop 

left is incremeneted inside set only if a dupe is encountered then left iwll increment until the very next element after the dupe - WHILE LOOP
right is incremented at each unique element outside WHILE LOOP


'''