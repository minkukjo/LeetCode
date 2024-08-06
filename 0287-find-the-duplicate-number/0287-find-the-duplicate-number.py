class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # print(slow,fast)
                break
                
        target = nums[0]
        
        while target != fast:
            target = nums[target]
            fast = nums[fast]

        return target
        