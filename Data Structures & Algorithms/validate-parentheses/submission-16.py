class Solution:
    def isValid(self, s: str) -> bool:
        elements = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for ele in s:
            if ele in elements:
                if stack and stack[-1] == elements[ele]:
                     stack.pop()
                else:
                    return False
            else:
               stack.append(ele)
        return True if len(stack)==0 else False
             