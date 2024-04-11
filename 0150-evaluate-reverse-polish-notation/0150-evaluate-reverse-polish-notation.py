from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operation = ["+", "-", "*", "/"]

        for token in tokens:

            if token in operation:
                second = stack.pop()
                first = stack.pop()
                
                temp = 0
                if token == "+":
                    temp = first + second
                elif token == "-":
                    temp = first - second
                elif token == "*":
                    temp = first * second
                else:
                    temp = int(first / second)
                stack.append(temp)
            else:
                stack.append(int(token))
                
        
        
        return stack.pop()
