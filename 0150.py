class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num1) + int(num2)
                stack.append(str(res))
            elif x == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2) - int(num1)
                stack.append(str(res))
            elif x == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num1) * int(num2)
                stack.append(str(res))
            elif x == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2) / int(num1)
                stack.append(str(int(res)))
            else:
                stack.append(x)
        return stack.pop()