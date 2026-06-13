class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""
        arr1 = [chr(i) for i in range(ord("a"),ord("z")+1)]
        arr3 = [chr(i) for i in range(ord("A"),ord("Z")+1)]
        arr2 = [str(i) for i in range(0,10)]
        for i in s:
            if i == " ":
                continue
            if i in arr1 or i in arr3:
                str1+=i.lower()
            if i in arr2:
                # print(i)
                str1+=i

        # print(str1,str1)
        if str1 == str1[::-1]:
            return True 
        else:
            return False