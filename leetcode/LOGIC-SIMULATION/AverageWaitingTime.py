'''1701. Average Waiting Time
Solved
Medium
Topics
Companies
Hint
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.'''

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        waiting_time = 0
        prevtime = customers[0][0]#initiating prevtime as the first arrivaltime of the person
        total_waiting_time = 0


        for a,p in customers:
            if a > prevtime:#if the person arrived later than the entire time the cook was busy
                #prevtime indicates the balance time the cook is remaining busy
                #but if you come so late - then its like cook immediately serves you 
                prevtime = a#so your arrival time becomes automatically the cook's work start time
            time_taken_to_cook = prevtime + p#prevtime stands for
            #the time cook was cooking for like previous custyomer, p is your dish cook time
            waiting_time = time_taken_to_cook - a#waiting time is direct 
            print(waiting_time)
            total_waiting_time += waiting_time
            print(total_waiting_time)
            prevtime = time_taken_to_cook#prevtime for a new customer
            #almost always is the second when previous food got delivered - 
            #which will be equal to that prev person's cooktime 

        avg_wait_time = float(total_waiting_time)/float(len(customers))#this is important i guess
        print(avg_wait_time)
        return avg_wait_time

'''
this is pretty neat code - only small problem but when you see two testcases and the
method of solving - karyangal petennuy kathum
'''
#below is smaller solution
class Solution:
    def averageWaitingTime(self, customers) -> float:
        available_at = 0
        total_wait = 0
        for arrival, t in customers:
            available_at = max(available_at, arrival) + t
            total_wait += available_at - arrival
        
        return total_wait / len(customers)