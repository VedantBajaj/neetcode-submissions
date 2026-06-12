class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]]
        post_sum = []
        num1 = nums[0]
        num2 = 1
        ret = []
        for i in range(1,len(nums)-1):
            num1*=nums[i]
            pre_sum.append(num1)
        pre_sum = [1]+pre_sum[::]
        for i in range(len(nums)-1,0,-1):
            num2*=nums[i]
            post_sum.append(num2)
        post_sum= post_sum[::-1]+[1]
        # print(pre_sum)
        # print(post_sum)
        for i in range(len(nums)):
            ret.append(pre_sum[i]*post_sum[i])
        return ret