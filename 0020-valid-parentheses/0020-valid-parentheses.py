class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if (bracket == ')' and stack[-1] == '(') or (bracket == ']' and stack[-1] == '[') or (bracket == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
