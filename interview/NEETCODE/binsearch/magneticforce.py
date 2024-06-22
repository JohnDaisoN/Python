'''
fuck i thought i was cooking smth 
\PROBLEM

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.


MY HTOUGHTS
i thought that minimum force can be maximized if a ball is kept in correct middle of each subarray recursively

but thats not needed - 

i figured out binary search

but bs is not doneon pos array , rather on force 

where l = min force betwen 2 balls cn be 1
 r= max force = max element - min element ig


'''
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        pos = sorted(position)
        l = 0
        r = len(pos)-1
        m -= 2
        mid = l + ((r-l)//2)
        if m:
            while m and l<=r:
            
                
                m -= 1
                r = mid 
        l = mid+1
        r = len(pos)-1

        if m:
            while m and l <= r:
                m -= 1#stupid solitions o i thought of recursive backtracking etc

            
                l = mid+1

#actual solition

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def possibleToPlace(mid, pos, m):#just like mindaysforbouque a
            #helper function to decide if the particular condition is true or not 
            prev = pos[0]#position default for first magnet
            countBalls = 1#first magnet ball is placed so...

            for i in range(1, len(pos)):#for remaining magnets
                curr = pos[i]#we place next magnet in next position[i]
                if curr - prev >= mid:#check magnetic force - if > than or = mid 
                    #only then we can place the ball there or else our minimum force 
                    #is not maximized 
                    countBalls += 1
                    prev = curr# saving current position as new prcious for next prev
                
                if countBalls == m:
                    break

                
            return countBalls == m#true condition evalucated if all balls are placed or not


        pos = sorted(position)
        
        l = 1#min force between balls possible 
        r = pos[-1] - pos[0]# max force possible only betwen extremen elements of sorted array
        result = 0
        while l <= r:#remaining same logic as bouquet i guess
            mid = l + ((r-l)//2)
            if possibleToPlace(mid, pos, m):
                result = mid
                l = mid + 1
            else:
                r = mid-1
                
        return result
            
        
        

            


        return abs(pos[r] - pos[l])


        

                
            
        
        

            


        return abs(pos[r] - pos[l])


        