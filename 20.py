"""17/01/25"""
derived1 = [1,1,0]
derived2 = [1,1]
derived3 = [1,0]
class Solution:
    def doesValidArrayExist(self, derived):
        res = 0
        for n in derived:
            res ^= n
        return res == 0
sol = Solution()
print(sol.doesValidArrayExist(derived1)) #True
print(sol.doesValidArrayExist(derived2)) #True
print(sol.doesValidArrayExist(derived3)) #False
#✅✅

