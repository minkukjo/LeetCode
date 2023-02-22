class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token =='/':
                two = stack.pop()
                one = stack.pop()

                if token == '+':
                    stack.append(one + two)
                elif token == '-':
                    stack.append(one - two)
                elif token == '*':
                    stack.append(one * two)
                else:
                    stack.append(int(float(one)/two))
            else:
                stack.append(int(token))
        return stack.pop()
    
