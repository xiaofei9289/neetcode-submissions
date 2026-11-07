class Solution:
    def isValid(self, s: str) -> bool:
        map = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for ele in s:
            if ele in map:
                if stack and stack[-1] == map[ele]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(ele)   

        n = len(stack)
        if n == 0:
            return True
        else:
            return False     