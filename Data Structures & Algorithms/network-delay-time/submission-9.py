class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float("inf")

        distance_table = []
        for i in range(n+1):
            row = [INF] * (n+1)
            distance_table.append(row)
        
        for node in range(1, n+1):
            distance_table[node][node] = 0
        
        for start, end, edge in times:
            distance_table[start][end] = min(distance_table[start][end],edge)
        
        updated_distances = [INF] * (n+1)
        visited_node = [False] * (n+1)
        updated_distances[k] = 0

        for _ in range(n):
            cur_node = -1
            min_dinstance = INF

            for node in range(1, n+1):
                if not visited_node[node] and updated_distances[node] < min_dinstance:
                    min_dinstance = updated_distances[node]
                    cur_node = node
            if cur_node == -1:
                break

            visited_node[cur_node] = True

            for neighbor_node in range(1, n+1):
                if visited_node[neighbor_node]:
                    continue
                new_distance = updated_distances[cur_node] + distance_table[cur_node][neighbor_node]

                if new_distance < updated_distances[neighbor_node]:
                    updated_distances[neighbor_node] = new_distance

        max_time = max(updated_distances[1:])

        if max_time == INF:
            return -1

        return max_time      
