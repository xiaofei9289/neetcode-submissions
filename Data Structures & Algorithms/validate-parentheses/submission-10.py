class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for ele in s:
            if ele in pairs:
                if stack and stack[-1]==pairs[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        return stack==[]

                
        
        