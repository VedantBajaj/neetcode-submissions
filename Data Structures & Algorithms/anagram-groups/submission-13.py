class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            arr1 = [0 for _ in range(26)]
            for j in i:
                arr1[ord(j)-ord("a")]+=1
            if tuple(arr1) in dict1:
                dict1[tuple(arr1)].append(i)
            else:
                dict1[tuple(arr1)]= [i]
        return list(dict1.values())