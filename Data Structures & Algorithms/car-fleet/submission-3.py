class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=sorted(list(zip(position,speed)),reverse=True)
        stack=[]
        for pos, spe in pairs:
            time=(target-pos)/spe
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)

        