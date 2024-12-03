s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
s2 = "icodeinpython"
spaces2 = [1,5,7,9]
s3 = "spacing"
spaces3 = [0,1,2,3,4,5,6]

class Solution:
    def add_spaces(self,s, spaces):
        res = ""
        prev = 0
        for i in range(len(spaces)):
            res += s[prev:spaces[i]] + " "
            prev = spaces[i]
        res += s[prev:]

        return res

sol = Solution()
print(sol.add_spaces(s, spaces))
print(sol.add_spaces(s2, spaces2))
print(sol.add_spaces(s3, spaces3))