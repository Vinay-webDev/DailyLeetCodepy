"""09/01/25"""
words1, pref1 = ["pay","attention","practice","attend"], "at"
words2, pref2 = ["leetcode","win","loops","success"], "code"
class Solution:
    def prefixCount(self, words, pref):
        N = len(words)
        count = 0
        for i in range(N):
            prefix = words[i][:len(pref)]
            if pref in prefix:
                count += 1
        return count
sol = Solution()
print(sol.prefixCount(words1, pref1))   #2
print(sol.prefixCount(words2, pref2))   #0

