class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator=["+","-","*","/"]
        for ele in tokens:
            if ele in operator:
                right = stack.pop()
                left = stack.pop()

                if ele == "+":
                    res = left + right
                elif ele == "-":
                    res = left - right
                elif ele == "*":
                    res = left * right
                else:
                    res = abs(left) // abs(right)
                    if (left < 0) != (right < 0):
                        res = -res
                
                stack.append(res)
            else:
                stack.append(int(ele))
        return stack[-1]
