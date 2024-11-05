s1 = "1001"
s2 = "0000"
s3 = "10"
s4 = "1010101010"
class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(0, len(s), 2):
            if (s[i] != s[i+1]):
                changes += 1
            
        return changes

sol = Solution()
print(sol.minChanges(s1))
print(sol.minChanges(s2))
print(sol.minChanges(s3))
print(sol.minChanges(s4))