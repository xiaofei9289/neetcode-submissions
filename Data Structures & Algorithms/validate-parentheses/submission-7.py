class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_brackets={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        if len(s)%2!=0:
            return False
        for ele in s:
            if ele in close_brackets:
                if stack and stack[-1]==close_brackets[ele]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(ele)
        return True if not stack else False
        