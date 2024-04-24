class Solution(object):
 def numIdenticalPairs(self, nums):
        '''n = sorted(nums)
        count = 0
        for l in range(0,len(n)-1):
                
            
                if n[l] == n[l+1]:
                    count += 1
                else:
                    l = count + 1
                
        return count'''
       

        num_count = {}
    
    
        good_pair_count = 0
    

        for num in nums:
            if num in num_count:

                num_count[num] += 1
            else:

                num_count[num] = 1
    

        for count in num_count.values():
            good_pair_count += (count * (count - 1)) // 2  # 
        
        return good_pair_count