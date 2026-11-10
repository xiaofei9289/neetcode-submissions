class Solution:
    def isValid(self, s: str) -> bool:
        ele_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for ele in s:
            if ele in ele_map:
                if stack and ele_map[ele] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(ele)
        
        return True if len(stack)==0 else False