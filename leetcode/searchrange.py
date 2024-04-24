class Solution(object):
 def searchRange(self, nums, target):
    
     list = []
     count = nums.count(target)
     if len(nums) == 1:
         if count == 1:
             return [0,0]
         else:
             return [-1,-1]
     elif len(nums) > 1:
            #return [0,0]
        if count == 1:
            a = nums.index(target)
            return [a,a]

        

        elif count > 1:
            a = nums.index(target)
            list.append(a)
            for i in range(count-1):
                
                a += 1
            list.append(a)
            return list
        
     return [-1,-1]