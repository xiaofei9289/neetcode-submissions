class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair[temp, index]

        for i in range(len(temperatures)):
            today_temp=temperatures[i]

            while len(stack) > 0:
                previous_temp = stack[-1][0]
                previous_day = stack[-1][1]

                if today_temp > previous_temp:
                    res[previous_day] = i - previous_day
                    stack.pop()
                else:
                    break
            stack.append([today_temp, i])
        return res