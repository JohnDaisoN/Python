'''
malayalam - aiyeeeeee

ithneth mairu

all elements will be only size 2, so take any 2 elements , see which one is present in both
return that

aiyeee

'''
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges:
            a = edges[0][0]
            b = edges[0][1]
            if a in edges[1]:
                return a
            else:
                return b
    '''
   basically another long approach for 0{n} will be finding degree of each vertex - and see 
   which ones becomes n-1 . :,//
    '''