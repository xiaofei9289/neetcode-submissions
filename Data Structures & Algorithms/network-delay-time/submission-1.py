
class Solution:
    def networkDelayTime(self, times, n, k):
        INF = float('inf')

        # 1. 初始化距离矩阵
        dist = [[INF] * (n + 1) for _ in range(n + 1)]

        # 2. 自己到自己的距离是 0
        for i in range(1, n + 1):
            dist[i][i] = 0

        # 3. 添加有向边
        for u, v, w in times:
            dist[u][v] = min(dist[u][v], w)

        # 4. Floyd 算法
        for mid in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][mid] + dist[mid][j]
                    )

        # 5. 只取起点 k 对应的那一行
        ans = max(dist[k][1:])

        return -1 if ans == INF else ans
