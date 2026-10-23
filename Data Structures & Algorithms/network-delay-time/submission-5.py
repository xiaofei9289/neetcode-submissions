
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        INF = float('inf')

        # 1. 初始化二维距离矩阵
        # distances[i][j] 表示节点 i 到节点 j 的最短距离
        distances = [[INF] * (n + 1) for _ in range(n + 1)]

        # 2. 节点到自己的距离为 0
        for node in range(1, n + 1):
            distances[node][node] = 0

        # 3. 记录所有直接连接的有向边
        for source_node, target_node, travel_time in times:
            distances[source_node][target_node] = min(
                distances[source_node][target_node],
                travel_time
            )

        # 4. Floyd 核心：三层循环
        # 第一层：枚举中转节点
        for middle_node in range(1, n + 1):

            # 第二层：枚举起点
            for source_node in range(1, n + 1):

                # 第三层：枚举终点
                for target_node in range(1, n + 1):

                    # 经过中转节点的新距离
                    new_distance = (
                        distances[source_node][middle_node]
                        + distances[middle_node][target_node]
                    )

                    # 如果经过中转节点更短，就更新
                    distances[source_node][target_node] = min(
                        distances[source_node][target_node],
                        new_distance
                    )

        # 5. 取起点 k 到所有节点的最短距离
        max_time = max(distances[k][1:])

        # 6. 有不可达节点返回 -1
        return -1 if max_time == INF else max_time
