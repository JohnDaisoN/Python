'''
os bascially
this is simple to think about

TOUGHITY TOUHH TOGUHGHGHGTHT

TOUGHEST SLIDING WINFOW FOR NEETCODE SPECIAL MENTION
'''

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = 0
        length = 0
        slid_length = []
        # current_max = 0
        # current_min = math.inf
        ma,mi = nums[0],nums[0]
        slid_length.append(nums[0])
        for r in range(1,len(nums)):
            if nums[r] > ma:
                ma = nums[r]
            elif nums[r] <= mi:
                mi = nums[r]
            
            
            if ma - mi <= limit:
                slid_length.append(nums[r])
                length = max(length, len(slid_length))
                print(slid_length)

                continue
            else:
                while ma - mi > limit:
                    
                    slid_length.remove(slid_length[0])
                    # l += 1
        return length


                



    
        '''
code explanation requires a vit of work

so min_q stores min elements in montonically increasing fashion
[1,2,3] so we need to pop an element from min_q iff that element is smaller than the last element

the logic here is that
we add like 1,2, 4 etc - so now 4 is the min element in worst case 
but then we encounter like 3
then we can pop 4 because 4 will never be a min_element as long as we haev 3 in our consideration


similaerly in max_heap, it is monotonically decreasing - 3,2,1
so if an element bigger than last element comes - pop and append

after while conditions
'''
        min_q = deque()
        max_q = deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            
            min_q.append(nums[r])#this happend nonetheless bcuz min_q has been popped enough
            #so that nums[r] becomes a valid choidce as last min element there
            max_q.append(nums[r])#simlr explnation as above
            
            while max_q[0] - min_q[0] > limit:#check for limit constraint
                #we check for characteristic of left element - which is like initially nums[0]
                if nums[l] == max_q[0]:#means it is the biggest element of current window
                    max_q.popleft()#we pop it from max_q so that now max_q's new first
                    #element is the second best big element 
                if nums[l] == min_q[0]:#same logic as above
                    min_q.popleft()#popleft because left number is minnnest
                l += 1
            res = max(res,r-l+1)#maximize logic

        

        return res


                



        