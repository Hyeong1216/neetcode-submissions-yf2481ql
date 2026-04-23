class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operator:
                num2 = stack.pop()
                num1 = stack.pop()
                temp = 0
                if token == '+':
                    temp = num1 + num2
                elif token == '-':
                    temp = num1 - num2
                elif token == '*':
                    temp = num1 * num2
                else:
                    temp = int(num1 / num2)
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack[-1] if stack else 0
