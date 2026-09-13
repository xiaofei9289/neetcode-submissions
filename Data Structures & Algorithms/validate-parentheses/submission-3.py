class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele=="(" or ele =="{" or ele =="[":
                stack.append(ele)
            else:
                if not stack:
                    return False
                elif ele ==")" and stack.pop()!="(":
                    return False
                elif ele=="}" and stack.pop()!="{":
                    return False
                elif ele=="]" and stack.pop()!="[":
                    return False
        return False if stack else True
            