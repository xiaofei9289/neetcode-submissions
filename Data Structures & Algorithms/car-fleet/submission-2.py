class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        stack=[]
        for pos, spe in cars:
            time=(target-pos)/spe
            if not stack or time >stack[-1]:
                stack.append(time)
        return len(stack)
        