
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, value in enumerate(nums):
            dic[value] = i
        print(dic)

        for i, value in enumerate(nums):
            if target-value in dic and dic[target-value] != i:
                return [i, dic[target - value]]
        