class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split(' ')
        new_list = []
        #print list
        for word in list:
            w = (word[::-1])
            new_list.append(w)

        string = ' '.join(new_list)
        return string