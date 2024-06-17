'''502. IPO
Hard
Topics
Companies
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.'''

#finally here it is - hard - problem - 

'''
my logic - 

reading this makes it very much similar to resource allocation - bankers algorithm
thats it 
maybe i will sort the resources array - so that min req is first element itself

i tried coding up most of it - but find myself veering away - lot of conditions maybe
'''
# possible topics - greedy, heapmin, sorting etc
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        result = 0
        x = zip(capital, profit) # i thought to zip it up so that sorting based on capitals will also have corresponding profits info with it 
        count = 0
        
        if len(zip) > 1:
            while i < len(x)-1:# i thought comparing adjacent elements to check if resource needed for left = or < right
                # bevcause if equal then i need to first allot resource to the highest profiting firm because of condition of limited no : of projects 'k'
                if x[i][0] < x[i+1][0]:
                    if x[i][0] < w:
                        result += x[i][1]
                        i += 1
                    else:
                        return result
                elif x[i][0] == x[i+1][0]:
                    self
''' 
so lets see the NEETCODE i guess


luckily neetcode explained well
i understood hard code

pattern - TWO HEAP - MIN HEAP, MAX HEAP



'''

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        maxProfit = [] # only projects we can afford
        minCapital = [(c, p) for c, p in zip(capital, profits)] # MY LOGIC - we need to zip both arrays for non-indiced comparison
        heapq.heapify(minCapital) # this is a step which can be done with heap - 

        # default heapify function - makes minheap - root element is based on minimum capital


        
        for i in range(k): #because only k projects can be selected

            while minCapital and minCapital[0][0] <= w:# mincapital could be empty - means capital array was empty --- also --- root elements capital should be less
                # than current w or current capital
                c, p = heapq.heappop(minCapital)# pop the minimum capital element 
                heapq.heappush(maxProfit, -1 * p)# push the profit only to maxheap -- # tip - we multiply with -1 because doing that makes a maxheap instead
            if not maxProfit:# condition to check if first elements capital itself is bigger than current capital - then profit still is 0
                break
            w += -1 * heapq.heappop(maxProfit)# we add it to current capital and let the loop run again # -- again multiply with -1 to make it positive
        return w

        


        