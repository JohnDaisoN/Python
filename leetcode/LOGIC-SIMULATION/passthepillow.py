'''
2582. Pass the Pillow

There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds
'''
'''
Hey hello, I am here to talk about the problem in hand

So this problem pass the pillow, actually defences a lot of variables, namely doubletime,
deciding factor semi deci, sir, and answer to formally introduce this problem. 
We have to define what is actually happening here step-by-step. 

So I will take an example, case of NA is equal to 5 equal to N, which means there 
are five people with the first person holding the pillow at the zero second. 
So what happens is at first, second, first, the second person gets the pillow 
and so on till , the fourth second and the last person which is the fifth person
gets the pillow so what we realise here is that it only takes four seconds for
five people all to hold the pillow at least once

So in logical sense, we can inform that I NFER that it will take eight seconds 
in this case for a whole cycle to complete like the pillow starts from the first
person and ends with the first person back, but there are five people so what is 
the relation so here halfway trip takes four seconds, for is actually 5-1 and
therefore the eight seconds taken for a whole loop is actually 5-1 into two, 
so that’s what doubletime represents here doubletime equates to this number of 
seconds that taken for the pillow took complete a full site which will depend on 
the number of persons

Let’s get into the next round of action, or if we pen down two columns, the first 
column, indicating the number of seconds past and the second column, indicating the
person holding the pillow starting from the first person holding the pillow at the 
zero second and we go on writing this column for up to time equating to around 16/16
seconds Which is actually double of the loop time, which is it, which is eight. He
find a correlation that the first person in the line will hold the pillow at the
zero. Then the eight at last the 16 seconds, which are all multiples of eight, 
so the order of people holding the pillow from the 0 to the eight second, will
be as follows, 123454321, and this order will continue again and again you 
understand why we calculated a double type because this time is going to be 
used for as a factor. Because after this double time, the order is being 
repeated again and again, so easy, easy, easy, easy, we know in such situations
we use the model operator, duo modules modules to find which person holds the pillow, 
even if the time that is given exceeds the double time which we calculate so that
creates a big Segway into understanding what the deciding factor which is the
second variable in our code means the second way the deciding factor, sorry 
here requires the given time modulo double time, which means like if the time
that the code giving us is like 16 or 17 more Deloitte by the double time which
in here in this case, it is 8 so 1608, we will get zero, cancel and so on

No comes the if conditions, so if statement says that if this deciding factor is less 
than or equal to N minus one now, how did I arrive to this condition this was also 
realised because of me writing the two columns. So in this case N -1 refers to Four,
why do I want 4? If you had paid close attention, you would see the order that is 
123454321 goes increasing till five and then decreases andthis 5 occurs when at the
fourth second, so from 0 to 4 seconds, the person holding the pillow would be the 
result from the modulo which is the deciding factor plus one ECEC easy enough

No else condition that is more lines of court, if I miss here, we see the third page
variable semi decisor hello I need this semi dicier because I notice that from times
5 to 7, the person holding decreases from 432 so I needed some relation correlating
5 to 47 to 3 and 623 and 72, so we know that 5-1 is 46-33 and 7-5 gifts two so 135 
is a pattern, which is the odd numbers, right, where one can be presented as two 
into 0+ one, three is equal to 2× one plus one and five is equal to 2×2+ one in 
this equation, only change is the multiplication factor 01 and two, so I want to
get result as 0 for 5, 1 for 6 and 2 for 7. so I thought can I modulo the deciding
factor which I got as 56 and seven with some other new factor which then struck 
it then struck me. I can just more below this deciding factor with four because 
5%4 is one six model four is to and, 7%4 is three, and now this result only needs
to be subtracted by one to get zero one and two so now

So now the last variable answer can be expressed as deciding factor minus the odd
number which we get from the semi decisive that line can be understood easily from 
a explanation. That’s it. I got like a run time of 10 million seconds only which
means it’s pretty efficient and the memory is also pretty efficient. It will also 
reach 80 8090% so basically constant memory becausewe are not using any RIS on we
everything is basically constant variables. A basic condition so, also shouldn’t
be that high. Maybe I can do some comprehension for this condition to reduce number
 of friends, but this is pretty readable. I might change the names.
'''
class Solution(object):
    def passThePillow(self, n, time):
        #doubletime refers to the constant gotten by multiplyinh noof person - 1 by 2
        doubletime = (n-1)* 2

        decidingfactor = time % doubletime
        if decidingfactor <= (n-1):
            return decidingfactor + 1
        else:
            semidecisor = decidingfactor % (n-1)
            answer = decidingfactor - (2*(semidecisor-1)+1)
            return answer
'''
so basiclaly above program can be solved only if you have clear sense of minf

so many variables and modulus ops games

i felt it like between easy and medium

doable in an interview with a vlear state of minf


refer mP-5 SUMMER BIRD BOOK last page for some extra inference
'''