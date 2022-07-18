class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for bracket in s:    
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if len(stack) == 0 and (bracket == ')' or bracket == ']' or bracket == '}'):
                    return False
                elif (bracket == ')' and stack[-1] == '(') or (bracket == ']' and stack[-1] == '[') or (bracket == '}' and stack[-1] =='{'):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True