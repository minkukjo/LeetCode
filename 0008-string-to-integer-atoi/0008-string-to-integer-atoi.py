class Solution:
    def myAtoi(self, s: str) -> int:
        
        if s == "":
            return 0
        
        
        result = ""
        isStartNumber = False
        isMinus = False
        for i in range(len(s)):
            if isStartNumber == True and s[i] == " ":
                break
            elif isMinus == True and s[i] == " ":
                return 0
            elif s[i] == " ":
                continue
            elif isMinus == False and isStartNumber == False and (s[i] == '-' or s[i] == '+'):
                isMinus = True
                result += s[i]
            elif isStartNumber == False and isMinus == True and (s[i] == '+' or s[i] == '-'):
                return 0
            elif isStartNumber == False and s[i].isdecimal() != True:
                break
            elif isStartNumber == True and s[i].isdecimal() != True:
                break
            elif s[i].isdecimal():
                result += s[i]
                isStartNumber = True
                
        if len(result) == 1 and result[0].isdecimal() != True:
            return 0
        if result == "":
            return 0
 
        if int(result) > 2**31 - 1:
            result = 2**31 - 1
        elif int(result) < -2**31:
            result = -2**31
            
        return int(result)
            




