class Solution:
    def isValid(self, s: str) -> bool:
        res= {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack=[]
        for ele in s:
            if ele in res:
                if stack and stack[-1]==res[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        return True if not stack else False