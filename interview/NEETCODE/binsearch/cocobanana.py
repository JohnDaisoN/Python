'''
i didnt code

the concepts i got before glancing st sol

1) min would be 1, max would be max(piles)- because the min no of hours alloted will be atleast the size ofpiles - so in that conditon
we need the rate to be max element because we need to finish that pule in max 1 hour

the thing i got - 
1) time taken would be just ceiling value of the pile size divided by rate 0 adec umualtively
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
