
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # 1. 最小堆：(连接费用, 节点编号)
        minHeap = [(0, 0)]

        # 2. 记录已经连接的节点
        visited = set()

        # 3. 总费用
        res = 0

        # 4. 每次选择费用最小的边
        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            # 5. 将当前节点加入生成树
            visited.add(node)
            res += cost

            # 6. 遍历所有未连接的节点
            x1, y1 = points[node]

            for nei in range(n):
                if nei not in visited:
                    x2, y2 = points[nei]

                    # 7. 计算曼哈顿距离
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    # 8. 将候选连接放入最小堆
                    heapq.heappush(minHeap, (dist, nei))

        return res
