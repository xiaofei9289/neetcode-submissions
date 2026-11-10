class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = ["+", "-", "*", "/"]
        stack = []

        for ele in tokens:
            if ele not in operation:
                stack.append(int(ele))
            else:
                a = stack.pop()
                b = stack.pop()
                if ele == "+":
                    res = a + b
                elif ele == "-":
                    res = b - a
                elif ele == "*":
                    res = a * b
                else:
                    res = int(b/a)
                stack.append(res)
        return stack[0]