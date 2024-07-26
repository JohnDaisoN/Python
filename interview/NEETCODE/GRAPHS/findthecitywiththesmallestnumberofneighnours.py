'''

Code
Testcase
Test Result
Test Result
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
Solved
Medium
Topics
Companies
Hint
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''

#djikstras solutin - pretty trivial i guess - but above medium i BET
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        #basically an adjacency matrix
        adj = defaultdict(list)
        for u,v,dist in edges:
            adj[u].append((v,dist))
            adj[v].append((u,dist))
        def djikstra(src):
            heap = [(0,src)]
            visit = set()
            while heap:
                dist,node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei,dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap,(nei_dist,nei))

            return len(visit)-1
        min_count = float("inf")
        res = -1
        for src in range(n):
            count = djikstra(src)
            if count <= min_count:
                res,min_count = src,count
        return res

