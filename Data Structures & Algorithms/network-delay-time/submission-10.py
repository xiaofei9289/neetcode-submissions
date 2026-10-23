class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float("inf")

        adj = defaultdict(list)

        for start_node, end_node, edge_weight in times:
            adj[start_node].append((end_node,edge_weight))

        shortest_distances = [INF] * (n+1)
        shortest_distances[k] = 0

        min_heap = [(0,k)]
        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_time > shortest_distances[cur_node]:
                continue
            for neighbor_node, edge_weight in adj[cur_node]:
                new_distance = cur_time + edge_weight

                if new_distance < shortest_distances[neighbor_node]:
                    shortest_distances[neighbor_node] = new_distance
                    heapq.heappush(
                        min_heap,
                        (new_distance, neighbor_node)
                    )
        max_time = max(shortest_distances[1:])

        return -1 if max_time == INF else max_time



