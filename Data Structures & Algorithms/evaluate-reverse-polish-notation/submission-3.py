class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele == "+":
                right, left = stack.pop(), stack.pop()
                stack.append(right + left)
            elif ele == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif ele == "*":
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            elif ele == "/":
                right, left = stack.pop(), stack.pop()
                stack.append(int(float(left)/right))
            else:
                stack.append(int(ele))
        return stack[-1]
        