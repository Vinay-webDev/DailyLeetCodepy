"""04/01/25"""

# class Solution:
#     def countPalindromicSubsequence(self, s):
#         arr = list(s)
#         n, count = len(arr), 0
#         l, r = 0, n - 1
#         sett = set(s)
#         mid = n // 2
#         while l < r and l != mid and r != mid:
#             if arr[l] == arr[r]:
#                 count += 1
#                 l += 1
#                 r -= 1

class Solution:
    def countPalindromicSubsequence(self, s):
        count, n = 0, len(s)
        sett = set(s)
        if n < 3:
            return 0
        for mid in sett:
            l, r = 0, n - 1
            while l < r:
                if s[l] == s[r]:
                    for i in range(l + 1, r):
                        if s[i] == mid:
                            count += 1
                            break
                    l += 1
                    r -= 1
                else:
                    if s[l] < s[r]:
                        l += 1
                    else:
                        r -= 1
        return count
# sol = Solution()
# print(sol.countPalindromicSubsequence(s1))  #3
# print(sol.countPalindromicSubsequence(s2))  #0
# print(sol.countPalindromicSubsequence(s3))  #4
# print(sol.countPalindromicSubsequence(s3))  #2  ❌WRONG ANSWER❌
s1 = "aabca"
s2 = "adc"
s3 = "bbcbaba"
s4 = "uuuuu"       
class Solution:
    def countPalindromicSubsequence(self, s):
        count, n = 0, len(s)
        sett = set(s)
        for mid in sett:
            l, r = 0, n - 1
            while l < n and s[l] != mid:
                l += 1
            while r >= 0 and s[r] != mid:
                r -= 1
            if l < r:
                count += len(set(s[l + 1:r]))
        return count
sol = Solution()
print(sol.countPalindromicSubsequence(s1))  #3
print(sol.countPalindromicSubsequence(s2))  #0
print(sol.countPalindromicSubsequence(s3))  #4
print(sol.countPalindromicSubsequence(s4))  #1

#✅✅✅✅