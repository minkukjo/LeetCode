class Solution:
    def addBinary(self, a: str, b: str) -> str:

        while len(a) != len(b):
            if len(a) > len(b):
                b = "0" + b
            else:
                a = "0" + a
        
        answer = ""
        over = 0
        for i in range(len(a)-1, -1, -1):
            digit = 0
            if int(a[i]) + int(b[i]) + over == 2:
                over = 1
            elif int(a[i]) + int(b[i]) + over == 3:
                over = 1
                digit = 1
            else:
                digit = int(a[i]) + int(b[i]) + over
                over = 0

            answer = str(digit) + answer
        
        if over != 0:
            answer = str(over) + answer
        return answer






