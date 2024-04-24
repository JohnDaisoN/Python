class Solution(object):
    def winnerOfGame(self, colors):
        alice,bob = 0,0
        #l = 0

        for i in range(1,len(colors)-1):
            #if colors[l] != colors[r]:
               # l = r
            #extra = r - l + 1 - 2

            if colors[i-1] == colors[i] == colors[i+1]:
                #if extra > 0:
                    if colors[i] == 'A':
                        alice += 1
                    else:
                        bob += 1

        return alice > bob