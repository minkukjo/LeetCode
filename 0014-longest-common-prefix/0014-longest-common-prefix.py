class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        index = 0

        first = ""

        answer = ""

        min_length = float('inf')
        for str in strs:
            min_length = min(min_length, len(str))
        
        while index < min_length:

            isSame = True
            for str in strs:
                if first == "":
                    first = str[index]
                elif first != str[index]:
                    isSame = False
                    return answer
            if isSame == True:
                index += 1
                answer += first
                first = ""
        return answer
