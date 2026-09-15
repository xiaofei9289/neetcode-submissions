class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 将位置和速度配对，再按位置从大到小排序
        cars = sorted(zip(position, speed), reverse=True)

        res = 0
        fleet_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > fleet_time:
                res += 1
                fleet_time = time

            # 否则追上前面的车队，不需要做任何操作

        return res