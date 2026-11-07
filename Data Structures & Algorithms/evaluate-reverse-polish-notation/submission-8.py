class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []
        for ele in tokens:
            if ele not in operator:
                stack.append(int(ele))
            else:
                num2,num1 = stack.pop(),stack.pop()
                if ele == "+":
                    res = num1 + num2

                elif ele == "-":
                    res = num1 - num2

                elif ele == "*":
                    res = num1 * num2

                else:
                    res = int(num1 / num2)

                stack.append(res)
        return stack[0]