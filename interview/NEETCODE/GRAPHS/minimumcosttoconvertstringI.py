'''

Topics
Companies
Hint
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost
'''
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        adj = defaultdict(list)
        for src,dst,cost in zip(original, changed,cost ):
            adj[src].append((dst,cost))

        def djikstra(src):
            heap = [(0,src)]
            dist_node = {}
            while heap:
                dist,node = heapq.heappop(heap)
                if node in dist_node:
                    continue
                dist_node[node] = dist
                for nei,nei_cost in adj[node]:
                    heapq.heappush(heap,(dist+nei_cost, nei))
            return dist_node


        res = 0

        min_cost = {elem:djikstra(elem) for elem in set(source)}
        for src,dst in zip(source,target):
            if dst not in min_cost[src]:
                return -1
            res += min_cost[src][dst]
        return res

        
