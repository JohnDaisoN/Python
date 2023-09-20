def check(i,candies,extraCandies):
            i+= extraCandies
            return i >= max(candies)
            
            


result = map(lambda x:check(x,candies,extraCandies),candies)
print (result) 
   
"""
:type candies: List[int]
:type extraCandies: int
:rtype: List[bool]
        
def check(i, candies, extraCandies):
return i + extraCandies >= max(candies)
result = map(lambda x: check(x, candies, extraCandies), candies)
        
return list(result)   """
        