"""10/01/25"""
words1a = ["amazon","apple","facebook","google","leetcode"]
words2a = ["e","o"]
words1b = ["amazon","apple","facebook","google","leetcode"]
words2b = ["l","e"]
words1c = ["amazon","apple","facebook","google","leetcode"]
words2c = ["lo","eo"]
class Solution:
    def wordSubsets(self, words1, words2):
        res = []
        N, N2 = len(words1), len(words2)
        check = 0
        for i in range(N):
            for j in range(N2):
                if words2[j] not in words1[i]:
                    check = 0
                    break
                if words2[j] in words1[i]:
                    check += 1
                if check == N2:
                    res.append(words1[i])
                    check = 0
        return res
sol = Solution()
print(sol.wordSubsets(words1a, words2a))  #["facebook","google","leetcode"]
print(sol.wordSubsets(words1b, words2b))  #['apple', 'google', 'leetcode']
print(sol.wordSubsets(words1c, words2c))  #[]  ❌WRONG ANSWER❌



















