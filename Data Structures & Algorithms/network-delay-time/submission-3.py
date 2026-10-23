class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source_node, targent_node, time in times:
            adj[source_node].append((targent_node,time))
        

        shortest_distances = [float('inf')] * (n+1)
        shortest_distances[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_time > shortest_distances[cur_node]:
                continue
            for neighbor_node, edge_time in adj[cur_node]:
                new_time = cur_time + edge_time

                if new_time<shortest_distances[neighbor_node]:
                    shortest_distances[neighbor_node]=new_time
                    heapq.heappush(min_heap,(new_time,neighbor_node))
        max_time = max(shortest_distances[1:])
        if max_time == float('inf'):
            return -1
        return max_time
