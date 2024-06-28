'''
the topics forthe given problem is that heap, prioirty etc

i thought initially we could make a degree calculation with a 
dictionary
and give highest importance to each node 

then look adjacency list to get a proper idea of row index and column index of all roads
that are valid - 

but there is a problem when degree comes equal - the higher importance should go to the vertex 
that is associated wwiht maximum or smth ing like that
'''
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adjacency_list = {}
        degree = {}

        # Iterate over each road (edge) and populate the adjacency list and degree dictionary
        for road in roads:
            u, v = road
            if u not in adjacency_list:
                adjacency_list[u] = []
                degree[u] = 0
            if v not in adjacency_list:
                adjacency_list[v] = []
                degree[v] = 0
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        sorted_degree_desc = sorted(degree.items(), key=lambda item: item[1], reverse=True)

        importance = {}
        for node,deg in sorted_degree_desc:
            importance[node] = n
            n -= 1
            for node,deg in sorted_degree_desc:
                [node] = n
            n -= 1
        sum = 0
        
        for u,v in roads:
            sum += importance[u] + importance[v]
        return sum


        

        print(adjacency_list)

        print(importance)

'''
neetcode solition not even needed
luckily yeahhhhh!!1

'''
