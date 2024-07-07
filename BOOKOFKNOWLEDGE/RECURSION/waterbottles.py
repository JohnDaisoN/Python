'''There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 9, numExchange = 3'''

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        answer = numBottles
        # print(numBottles//numExchange)
        def recursivebottleelimination(nb,ne):

            # print(nb//ne)
            if nb < ne:
             return 0
            n = nb//ne
            remainingbottles = nb-(ne*n)
            addedbottles = remainingbottles + n

            
            return recursivebottleelimination(addedbottles,ne) + n
        # if numBottles < numExchange:
        #     return numBottles
            
        return answer + recursivebottleelimination(numBottles,numExchange)


        
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
'''
so basicallyi find this problem to be like between easy and medium


So basically, this is a request problem, recursion problem and it’s pretty easy
 when you have figured out the solution. I am actually happy because I actually
  managed to make the runtime of the solution 0 ms, which is a heck of a feet in 
  python, so the description is fairly easy, but I decided to code up the initial 
  solution using the first example where the number of water was nine and number
   exchange was three and output. We need is 13 and their explanation said that 13
    comes as 9+3+ one, so I thought there is some pattern here, like you take an
     umbrella bottles, and then I’m exchange, you divide them, which is 9÷3 get three
      then your recursively divided by the numb exchange so 3÷3. You get one so I 
      thought that until you get one something like that, but the problem with the 
      solution is that that only works for that that particular example alone, so my
       initial situation was recuring where the changed variable was the cent from 
       the floor division. I mean quotient.

But then I figured out when I submitted my solution, I seem to return an output which
 is always off by one or something like that, so I thought that could be solved by 
 carefully structuring the breaking condition. My initial condition was if the number
  of bottles left was less than number of portals to be exchanged , you can just 
  return one. That’s not the case.

The workout example is in my MP Saby book summer bird book back page, basically in 
this example of nine and three itself, what happens is you get nine bottles full? 
Save drink all of them that makes the number of bottles. You can drink as nine so 
now we know that at least a person can drink number of bottles that are given to 
them initially right that would be the minimum number that that he can drink , so
 now exchanged bottles number is three, and you have nine bottles left with 
 you empty, so you trade this nine bottles and get three filled ones and a cursive
  do this


Another interesting example, the problem is largely quantified is when number of
 bottles is 15 and numb exchange is for four here. The interesting details is that 
 four is not divisible by 15 unlike the previous example, here again first you bring 
 all the 15 bottles now you need to figure out for the next discussion. How many
  bottles you will be having , the idea is 15 empty bottles for the exchange factor.
 You have 4×3 equal to 12 bottles and 12 is divisible by four so you trade 12
bottles. You get three back full three full. So now the number of bottles become
the three empty ones left with you or, you think in this way you only drink 12
 of them and three are left full and these 12 are exchanged for three additional
  bottles. So now you have 3+3 equal to 6 so 6 is the number of bottles that 
should go to the next recursive court call, so my code cease to how the six
 comes to play. Breaking condition is when the number of water is become less
 than exchange factor. That is when you can return zero, because that is the
case when those are empty bottles which have already been considered the 
addition that’s it, thank you.
'''