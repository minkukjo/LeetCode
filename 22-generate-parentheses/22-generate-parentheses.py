class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def combiate(left, right, result):

            if left > right:
                return
            
            if left == 0 and right ==0:
                ans.append(result)
                return
            
            if left == 0:
                combiate(left, right - 1, result + ')')
            else:
                combiate(left-1, right, result + '(')
                combiate(left, right-1, result + ')')
        combiate(n,n,'')
        return ans
