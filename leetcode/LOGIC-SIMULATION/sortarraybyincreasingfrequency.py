class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        result = []
        for elem in nums:
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1

        ires = sorted(count.items(), key = lambda k:(k[1],k[0]))
        # print(iresult)
        i = 0
        while ires[i+1]!= None and i < len(ires):
            
            if ires[i][1] < ires[i+1][1]:
                for j in range(ires[i][1]):
                    result.append(ires[i][0])
                i += 1
            else:
                lower = i

                while ires[i+1] and ires[i][1] == ires[i+1][1]:
                    i += 1
                high = i
                newindex = i
                while high >= lower:
                    for j in range(ires[high][1]):
                        result.append(ires[high][0])
                    high -= 1
                i = newindex + 1

        

        return result


        
        # print(count)


'''
I tried doing above approach but it doesn't seem like a good one- it doea not even work 
i need to try learning counter( type) -maybe that's a good issue right??


'''
#counter type
