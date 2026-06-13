class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        for i in nums:
            cur = 1
            while i+1 in nums:
                cur+=1
                i+=1
            if cur>ret:
                ret = cur
        return ret