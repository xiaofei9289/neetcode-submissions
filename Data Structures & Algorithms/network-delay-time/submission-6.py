class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        distance_table = [[INF] * (n+1) for _ in range(n+1)]

        for node in range(1, n+1):
            distance_table[node][node] = 0

        for start_node, end_node, edge_weights in times:
            distance_table[start_node][end_node] = min(
                distance_table[start_node][end_node],
                edge_weights
            )
        
        for middle_node in range(1, n+1):
            for start_node in range(1, n+1):
                for end_node in range(1,n+1):
                    new_distance = distance_table[start_node][middle_node] + distance_table[middle_node][end_node]

                    distance_table[start_node][end_node] = min(distance_table[start_node][end_node],new_distance)
        max_distance = max(distance_table[k][1:])
        return -1 if max_distance == INF else max_distance