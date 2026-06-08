class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i<len(nums):
            new = target-nums[i]
            if new in nums[i+1:]:
                j = i+nums[i+1:].index(new)+1
                return [i,j]
            i+=1