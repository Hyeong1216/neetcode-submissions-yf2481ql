class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = ['+', '-', '*', '/']
        stack = []

        for i in range(len(tokens)):
            curr = tokens[i]
            if curr not in oper: #numbers
                stack.append(curr)
            else: #tokens
                n2, n1 = int(stack.pop()), int(stack.pop())
                result = 0
                if curr == "+":
                    result = n1 + n2
                elif curr == "-":
                    result = n1 - n2
                elif curr == "*":
                    result = n1 * n2
                else:
                    result = n1 / n2
                stack.append(result)
        return int(stack.pop())
            