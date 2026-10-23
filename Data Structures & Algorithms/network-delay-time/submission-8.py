class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float("inf")

        distance_table = []
        for i in range(n+1):
            row = [INF] * (n+1)
            distance_table.append(row)
        
        for node in range(1, n+1):
            distance_table[node][node] = 0

        for start, end, edge_weights in times:
            distance_table[start][end] = min(distance_table[start][end], edge_weights)
        
        shortest_distances = (n+1) * [INF]
        shortest_distances[k] = 0
        visited = [False] * (n+1)

        for _ in range(n):
            cur_node = -1
            min_distance = INF
            for node in range(1,n+1):
                if not visited[node] and shortest_distances[node]<min_distance:
                    min_distance = shortest_distances[node]
                    cur_node = node
            if cur_node == -1:
                break
            visited[cur_node] = True

            for neighbor_node in range(1,n+1):
                new_distance = shortest_distances[cur_node] + distance_table[cur_node][neighbor_node]
                if new_distance < shortest_distances[neighbor_node]:
                        shortest_distances[neighbor_node] = new_distance
        max_time = max(shortest_distances[1:])

        if max_time == INF:
            return -1

        return max_time
