'''

Code
Testcase
Testcase
Test Result
1380. Lucky Numbers in a Matrix
Solved
Easy
Topics
Companies
Hint
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
'''

#explanation in mp-5 greenbird book

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = [(i,0) for i in range(len(matrix[0]))]
        dic = dict(l)
        # print(dic)
        for elem in matrix:
            # minrowvalue = min(elem)
            # minindex = elem.index(minrowvalue)
            for i in range(len(elem)):
                # if dic[i] != 0:
                dic[i] = max(dic[i],elem[i])
                # else:
                    # dic[i] = elem[i]
            # dic[minindex] = max(dic[minindex],minrowvalue)
            # print(dic)
        # print(dic)
        mins = []

        for i in range(len(matrix)):
            mins.append( min(matrix[i]))

        # print(mins)

        result = [elem for elem in mins if elem in dic.values()]
        return result


        # result = [value for value in dic.values() if value != 0]
        # print(resul)t

        