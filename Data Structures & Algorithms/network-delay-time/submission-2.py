class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))

        dist = (n+1) * [float('inf')]
        dist[k] = 0
        heap = [(0,k)]

        while heap:
            d,u=heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans
