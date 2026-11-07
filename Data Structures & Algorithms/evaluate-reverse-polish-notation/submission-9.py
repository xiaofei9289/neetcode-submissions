class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {
            "+":lambda a,b:a+b,
            "-":lambda a,b:a-b,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(a/b)
        }
        stack = []

        for ele in tokens:
            if ele not in operator:
                stack.append(int(ele))
            else:
                a,b = stack.pop(),stack.pop()
                res = operator[ele](b,a)
                stack.append(res)

        return stack[0]

        