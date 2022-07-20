class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def genParent(s,left,right,result):
            if left: genParent(s+'(',left-1,right,result)
            if right>left:genParent(s+')',left,right-1,result) 
            if not right:
                result.append(s)
            return result
        
        return genParent('',n,n,[])