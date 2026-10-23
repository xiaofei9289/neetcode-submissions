class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf_values = float("inf")
        # initialize the 2D table with distance
        distance_table = []
        for i in range(n+1):
            row = [inf_values] * (n+1)
            distance_table.append(row)
        
        # assign 0 to distance between node and itself
        for node in range(1, n+1):
            distance_table[node][node] = 0
        # assign edge weights to the distance_table in corresponing position
        for start_node, end_node, edge_weights in times:
            distance_table[start_node][end_node] = min(distance_table[start_node][end_node], edge_weights)
        
        # apply floyd algorism

        for middle_node in range(1, n+1):
            for start in range(1, n+1):
                for end in range(1, n+1):
                    new_distance = distance_table[start][middle_node] + distance_table[middle_node][end]
                    # update distance 
                    distance_table[start][end] = min(distance_table[start][end], new_distance)
        max_time = max(distance_table[k][1:])
        return -1 if max_time == inf_values else max_time
        

        