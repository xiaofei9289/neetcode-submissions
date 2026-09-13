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
                if not stack:
                    return False
                if stack[-1]!=close_brackets[ele]:
                    return False
                stack.pop()
            
            else:
                stack.append(ele)
        return len(stack)==0
        