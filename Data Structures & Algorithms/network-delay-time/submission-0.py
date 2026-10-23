class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))
        min_heap = [(0,k)]
        visited = set()
        res = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = time

            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(
                        min_heap,
                        (time + weight, nei)
                    )
        return res if len(visited) == n else -1