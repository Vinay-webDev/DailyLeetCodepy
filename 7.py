"""01/01/25"""
s1 = "011101"
s2 = "00111"
s3 = "1111"
class Solution:
    def maxScore(self, s):
        maxx = 0
        left_sum = 0
        right_sum = 0
        for i in range(0, len(s)):
            if s[i] == "0":
                left_sum += 1
            for j in range(i+1, len(s)):
                if s[j] == "1":
                    right_sum += 1
            current_max = left_sum + right_sum
            maxx = max(maxx, current_max)
            left_sum = 0
            right_sum = 0
        return maxx
sol = Solution()
print(sol.maxScore(s1))
print(sol.maxScore(s2))
print(sol.maxScore(s3))
#❌❌WRONG ANSWER❌❌













