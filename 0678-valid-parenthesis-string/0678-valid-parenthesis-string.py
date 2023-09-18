class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        star = []
        for index, bracket in enumerate(s):
            if bracket == '(':
                stack.append(index)
            else:
                if bracket == '*':
                    star.append(index)
                else:
                    if len(stack) > 0:
                        stack.pop()
                    elif len(star) > 0:
                        star.pop()
                    else:
                        return False
            
        while stack and star:
            if stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                break
        return len(stack)==0

