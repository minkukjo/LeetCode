class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        dic = {}
        dic[2] = ['a','b','c']
        dic[3] = ['d','e','f']
        dic[4] = ['g','h','i']
        dic[5]= ['j','k','l']
        dic[6] = ['m','n','o']
        dic[7] = ['p','q','r','s']
        dic[8] = ['t','u','v']
        dic[9] = ['w','x','y','z']

        numbers = []
        for char in digits:
            numbers.append(dic[int(char)])

        result = []
        for item in product(*[number for number in numbers]):
            result.append("".join(item))
        return result