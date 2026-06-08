class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr1 = []
        arr_set = set()
        for i in nums:
            if i not in arr_set:
                arr_set.add(i)
                arr1.append([i,nums.count(i)])
        arr1 = sorted(arr1,key = lambda x : x[1],reverse = True)
        ret = []
        for i in range(k):
            ret.append(arr1[i][0])
        return ret
