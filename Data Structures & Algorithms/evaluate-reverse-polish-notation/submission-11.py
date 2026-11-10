class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)
        }
        stack = []
        for ele in tokens:
            if ele not in operations:
                stack.append(int(ele))
            else:
                a,b = stack.pop(),stack.pop()
                res = operations[ele](b,a)
                stack.append(res)
        return stack[0]