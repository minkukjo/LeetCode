class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin(l, r):
            if l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                
                return bin(l,r)
            return -1
        return bin(0, len(nums)-1)


