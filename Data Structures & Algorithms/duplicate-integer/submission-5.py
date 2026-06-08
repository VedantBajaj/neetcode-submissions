class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr1 = set()
        for i in nums:
            if i in arr1:
                return True
            else:
                arr1.add(i)
        return False