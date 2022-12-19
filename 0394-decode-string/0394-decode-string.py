class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curNum = 0
        curString= ""

        for c in s:
            if c == '[':
                stack.append(curNum)
                stack.append(curString)
                curString = ''
                curNum = 0
            elif c == ']':
                prev = stack.pop()
                num = stack.pop()
                curString = prev + curString * num
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


