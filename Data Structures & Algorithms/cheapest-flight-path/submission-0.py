
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        # 1. 初始化最低价格
        prices = [float('inf')] * n
        prices[src] = 0

        # 2. 最多 k 次中转 = 最多 k+1 次航班
        for i in range(k + 1):

            # 3. 复制上一轮的价格
            tempPrices = prices.copy()

            # 4. 遍历所有航班
            for u, v, price in flights:

                # 起点不可达，跳过
                if prices[u] == float('inf'):
                    continue

                # 5. 更新最低价格
                tempPrices[v] = min(
                    tempPrices[v],
                    prices[u] + price
                )

            # 6. 完成一轮更新
            prices = tempPrices

        # 7. 返回最终价格
        return prices[dst] if prices[dst] != float('inf') else -1
