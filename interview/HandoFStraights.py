'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.


'''
#my coded solution 
class Solution(object):
    def isNStraightHand(self, hand, groupSize):

        if len(hand) % groupsize == 0: #refers to checking if hands can be split into groupsize no of sets even saftel all
           sorted_hand = sorted(hand)#sorting to check for consecutively appearing values
           handdict = {}
           for elem in sorted_hand:
                count = sorted_hand.count(elem)
                handdict[elem] = count#making dict to store count of each occured value

           keys =  handdict.keys()
           l_index = 0
           r_index = l_index + groupSize
           onearray = [1 * groupSize]
           while r_index != len(keys)-1:
            if find_diff(keys[l_index:r_index]) == onearray:#extracting keys - checking like a sliding window for groupsize consecutive keys - find diff = [111111 etc] - then subtract the valueof the key - which could be the count
                for elem in keys[l_index:r_index]:
                    if handdict[elem]:
                        handdict[elem] -= 1
                    else:
                        del keys[l_index]
                    
            else:
                
                l_index+=1# if not found then increment both indices to forward the slid windoe
                r_index +=1

                
           


        
        #    for index,elem in enumerate(keys):
           


        

        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        

        #neetcode solution

        '''
        problem desc - look and draw out the scenario - check for a subsequence when a particular element
        is found - for ex -2 2 appear in start m and end

        also ooooo - 1 - or the minimum elemetn of hands can only appear as one scenario - [1,2,3] - greedy mayeb???



        explanation

        create a dict of keys and values sorted

        thenc comes tricky min-heap to search for the minimum balue in logn time - 
        becuz basically approach is to find the minimum value - decrement count by 1 - if count --= 0 - pop it off - minimum element always has only 1 way to be grouped thats
        when it comes first

        tree map used to search for arbitrary minimum element in logn bcuz you cant fo that in minheap

        '''

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)
        minH = list(count.keys())
        heapq.heapify(minH) # heapq structure for minheaping - mini element always at [0[ position]]
        while minH:
            first = minH[0]  #take min element
            for i in range(first, first+groupSize):  # take subsequence
                if i not in count:##means there is a leement discrepancy
                    return False
                else:
                    count[i] -= 1#found wanted element and decrement its count
                if count[i] == 0:
                    if i != minH[0]:# hole condition 
                        return False
                    heapq.heappop(minH)#STTTUUUDDYY HEAPPPOP METHODS
        return True