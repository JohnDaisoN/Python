'''
826. Most Profit Assigning Work
Attempted
Medium
Topics
Companies
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
'''

'''
this i dont think it is exactly a meidum problem - because it is very similar to hard iPO provlwm did previous;t

again 2 HEAP APPROACH

ALMOST SIMILAR CODE
just if you inderstand basics it works

but my solution - super high space complexity - i have to find other optimal solition

passed like 47  out of 52 testcases
'''
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        m = []
        
        # difpro =[(d,p) for d,p in  zip(difficulty, profit)]
        

        # heapify(difpro)
        
        # print(difpro)
        for elem in worker:
            profi = []
            difpro =[(d,p) for d,p in  zip(difficulty, profit)]
        

            heapq.heapify(difpro)

            while difpro and difpro[0][0] <= elem:
                
                d,p = heapq.heappop(difpro)
                print(d)
                print(p)
                heapq.heappush(profi, -1 * p)
            if not profi:
                continue
            w = -1 * heapq.heappop(profi)
            m = m + [w]
            print(m)
        
        return sum(m)

'''
optimal 

1st approach - heap

it was very similar to mine

what i didnt realizze is that to solve this problem

we can sort workers based on difficulty in reverse order - descending

then heap made wrt profit - maxheap so maximum profit element comes on top

then we pop until we see a tuple with d < worker's difficulty

so we reach a suitbale difficulty with max profit - that is correct profit fo rthat woeker

the key point is 
WORKERS COMING AFTER i TH WORKER CANNOT DO ANY JOB THAT iTH WORKER COULNT DO - BECAUSE THEY HAVE 
SMALLER DIFFICULTY

other impportant point
ONLY WORKS IF PROFIT PROPORTIONAL TO DIFFICULTY

'''
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # m = []
        s = 0
        difpro =[(-p,d) for p,d in  zip(profit,difficulty)]
        

        heapq.heapify(difpro)
        
        
        
        # print(difpro)
        for elem in sorted(worker, reverse = True):
            # profi = []
            # difpro =[(d,p) for d,p in  zip(difficulty, profit)]
        

            # heapq.heapify(difpro)

            while difpro and difpro[0][1] > elem:
                
                heapq.heappop(difpro)
                # print(d)
                # print(p)
                # heapq.heappush(profi, -1 * p)
            # if not profi:
                # continue
            if difpro:
                a,b = heapq.heappop(difpro)
                s += -a
                # print(m)
                heapq.heappush(difpro, (a,b))
        
        return s

'''
next approach

binary search woahh

we sort a d,p tuple array with ascending order

then for each worker
we do binary search - to find upto how much difficulty he can
do the work - get a subset of possible jobs

then sort it so as to get maximum profit - 

this can optimized 

by when first doing the sorting , profit part will be the maximum profit
uptil that index

this solves previous approach difficulty
'''

        



