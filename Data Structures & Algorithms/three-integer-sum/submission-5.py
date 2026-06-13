class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        target = 0
        ret = []
        for i in range(len(nums)):
            arr1 = []
            new = target - nums[i]
            for j in range(i+1,len(nums)):
                tar = new-nums[j]
                x = nums[j+1:]
                if tar in x:
                    arr1.append(nums[i])
                    arr1.append(nums[j])
                    arr1.append(tar)
                    if arr1 not in ret:
                        ret.append(arr1)
                    arr1 = []
        return ret


