class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={
            "+":lambda a,b:a+b,
            "-":lambda a,b:a-b,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(a/b)
        }
        for ele in tokens:
            if ele in operations:
                r,l=stack.pop(),stack.pop()
                res=operations[ele](l,r)
                stack.append(res)
            else:
                stack.append(int(ele))
        return stack[-1]
        