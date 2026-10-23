
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        INF = float('inf')

        # ========= 1. 构建邻接矩阵 =========

        # graph[i][j] 表示从节点 i 到节点 j 的时间
        # 初始化为无穷大，表示暂时没有直接连接
        graph = [[INF] * (n + 1) for _ in range(n + 1)]

        # 每个节点到自己的距离为 0
        for node in range(1, n + 1):
            graph[node][node] = 0

        # 把所有有向边加入邻接矩阵
        for source_node, target_node, travel_time in times:
            graph[source_node][target_node] = min(
                graph[source_node][target_node],
                travel_time
            )

        # ========= 2. 初始化距离和 visited =========

        # 记录起点 k 到每个节点的当前最短距离
        shortest_distances = [INF] * (n + 1)

        # 起点到自己的距离为 0
        shortest_distances[k] = 0

        # False 表示尚未确定最短距离
        # True 表示已经确定最短距离
        visited = [False] * (n + 1)

        # ========= 3. Dijkstra 主循环 =========

        # 最多确定 n 个节点
        for _ in range(n):

            # 当前轮要处理的节点
            current_node = -1

            # 寻找未访问节点中距离最小的节点
            for node in range(1, n + 1):

                # 只考虑未确定最短距离的节点
                if not visited[node]:

                    # 如果还没选中节点，或者发现更小的距离
                    if (current_node == -1 or
                        shortest_distances[node] <
                        shortest_distances[current_node]):

                        current_node = node

            # 如果剩余节点都无法到达，结束
            if (current_node == -1 or
                shortest_distances[current_node] == INF):
                break

            # ========= 4. 确定当前节点 =========

            # 当前节点的最短距离已经确定
            visited[current_node] = True

            # ========= 5. 松弛操作 =========

            # 遍历所有可能的邻居节点
            for neighbor_node in range(1, n + 1):

                # 已确定的节点不需要再次更新
                if visited[neighbor_node]:
                    continue

                # 当前节点到邻居没有直接连接
                if graph[current_node][neighbor_node] == INF:
                    continue

                # 通过当前节点到邻居的累计时间
                new_time = (
                    shortest_distances[current_node]
                    + graph[current_node][neighbor_node]
                )

                # 如果发现更短的路径，就更新距离
                if new_time < shortest_distances[neighbor_node]:
                    shortest_distances[neighbor_node] = new_time

        # ========= 6. 计算最终答案 =========

        # 忽略索引 0，取所有最短距离的最大值
        max_time = max(shortest_distances[1:])

        # 存在不可达节点
        if max_time == INF:
            return -1

        # 返回最后一个节点收到信号的时间
        return max_time
