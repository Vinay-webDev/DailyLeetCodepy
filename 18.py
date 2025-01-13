"""13/01/25"""
s1 = "abaacbcbb"
s2 = "aa"
s3 = "ecdxxxxhhhhhhhhhhhhhhbbfgfujjiisssjsjjs"
s4 = "ggggfhhfuhjsjiksjsjs"
class Solution:
    def minimumLength(self, s):
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        length = 0
        if len(s) < 3:
            return len(s)
        for c in count.values():
            if c < 3:
                length += c
            else:
                if c % 2 == 0:
                    length += 2
                else:
                    length += 1
        return length
sol = Solution()
print(sol.minimumLength(s1))    #5
print(sol.minimumLength(s2))    #2
print(sol.minimumLength(s3))    #17
print(sol.minimumLength(s4))    #12
#✅✅✅


