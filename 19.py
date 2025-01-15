"""14/01/25"""
#Brute force💪😤🔥
A1, B1 = [1,3,2,4], [3,1,2,4]
A2, B2 = [2,3,1], [3,1,2]
class Solution:
    def findThePrefixCommonArray(self, A, B):
        l, r = 0, 0
        res, count = [], 0
        while l < len(A) and r < len(B):
            for i in range(l + 1):
                if A[i] in B[:r + 1]:
                    count += 1
            res.append(count)
            count = 0
            l += 1
            r += 1
        return res
sol = Solution()
print(sol.findThePrefixCommonArray(A1, B1)) #[0, 2, 3, 4]
print(sol.findThePrefixCommonArray(A2, B2)) #[0, 1, 3]
#✅✅✅✅
#not efficient approach but it works










