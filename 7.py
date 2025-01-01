"""01/01/25"""

class Solution:
    def maxScore(self, s):
        maxx = 0
        left_sum = 0
        right_sum = 0
        for i in range(0, len(s)):
            if s[i] == "0":
                left_sum += 1
            for j in range(i + 1, len(s)):
                if s[j] == "1":
                    right_sum += 1
            current_max = left_sum + right_sum
            maxx = max(maxx, current_max)
            left_sum = 0
            right_sum = 0
        return maxx
# sol = Solution()
# print(sol.maxScore(s1))
# print(sol.maxScore(s2))
# print(sol.maxScore(s3))
#❌❌WRONG ANSWER❌❌

s1, s2 = "011101", "00111"
s3, s4 = "1111", "0101010"
class Solution:
    def maxScore(self, s):
        maxx = 0
        ones_count = s.count("1")
        left_sum = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_sum += 1
            if s[i] == "1":
                ones_count -= 1
            current_max = left_sum + ones_count
            maxx = max(maxx, current_max)
        return maxx
sol = Solution()
print(sol.maxScore(s1)) #5
print(sol.maxScore(s2)) #5
print(sol.maxScore(s3)) #3
print(sol.maxScore(s4)) #4










