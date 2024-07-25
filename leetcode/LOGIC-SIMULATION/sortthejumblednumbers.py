class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        mapp = {}
        for elem,pos in enumerate(mapping):
            mapp[str(elem)] = pos
        # print(mapp)
        mappednums = []
        for elem in nums:
            # print(list(elem))
            stringofnums = str(elem)
            mappedstringofnums = []

            for elem in stringofnums:
                mappedstringofnums.append( str(mapp[elem]))
            mappednums.append(''.join(mappedstringofnums))
        # print(mappednums)
        zipped = zip(mappednums, nums)
        # print(zipped)
        zipped.sort(key=lambda x: (int(x[0]), nums.index(x[1])))
        # print(result)
        actualresult = [elem[1] for elem in zipped]
        return actualresult
       

        
#fucking prblem - time limit exceeds hauntingly -let
#s fo to nenetcode solutin

#neetcode


        