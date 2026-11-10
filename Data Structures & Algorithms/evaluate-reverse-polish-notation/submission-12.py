class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for ele in tokens:
            if ele not in operations:
                stack.append(int(ele))
            else:
                b, a = stack.pop(),stack.pop()
                if ele == "+":
                    res = a + b
                elif ele == "-":
                    res = a - b
                elif ele == "*":
                    res = a * b
                else:
                    res = int(a/b)
                stack.append(res)
        return stack[0]

        