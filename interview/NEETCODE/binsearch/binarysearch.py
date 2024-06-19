class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = low + ((high - low) // 2)
        print(mid)

        while low < high:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                self.search( nums[0:mid], target)
            else:
                self.search( nums[mid+1:high], target)
        return -1
        
# above is not bin search - becasue not need of recursion 
#just a while loop and do it liek 2 pointers l, r , increment l , decrement r
'''
actual solution - is below

key point - mid is initiated inside loop as low + (high-low)/2 to avoid overflow error instead of low+high / 2
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
      
        

        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
        