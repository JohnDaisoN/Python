class Solution:
    def isPalindrome(self, s: str) -> bool:
        cased_string = s.lower()
        no_spaced_string = ''
        for elem in cased_string:
            if elem.isalnum():
                no_spaced_string+=elem

        # no_spaced_string = cased_string.replace(' ','')
        print(no_spaced_string)
        l, r = 0, len(no_spaced_string) - 1
        while l < r:
            if no_spaced_string[l] != no_spaced_string[r]:
                return False
            l, r = l + 1, r - 1
        return True
        

'''
interestingly isalnum() comes to the rescue to check for pumctaution marks
2 pointers l and r implemented and simple inc and dec works perfectly - npthong tooccrazy
'''