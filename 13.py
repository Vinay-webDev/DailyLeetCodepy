"""07/01/25"""

class Solution:
    def stringMatching(self, words):
        n = len(words)
        res = set()
        for i in range(n):
            for j in range(n):
                if i != j and words[j] in words[i]:
                    res.add(words[j])
        return [*res]
# sol = Solution()
# print(sol.stringMatching(words1))  #['hero', 'as']
# print(sol.stringMatching(words2))  #['et', 'code']
# print(sol.stringMatching(words3))  #[]
# print(sol.stringMatching(words4))  #['leetcode', 'od', 'am']

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Solution:
    def stringMatching(self, words):
        N = len(words)
        res = []
        for i in range(N):
            for j in range(N):
                if i != j and words[j] in words[i]:
                    res.append(words[j])
        return res
# sol = Solution()
# print(sol.stringMatching(words1))   #['hero', 'as']
# print(sol.stringMatching(words2))   #['et', 'code']
# print(sol.stringMatching(words3))   #[]
# print(sol.stringMatching(words4))   #['leetcode', 'od', 'am']

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
words1 = ["mass","as","hero","superhero"]
words2 = ["leetcode","et","code"]
words3 = ["blue","green","bu"]
words4 = ["leetcoder","leetcode","od","hamlet","am"]
class Solution:
    def stringMatching(self, words):
        N = len(words)
        res = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if words[j] in words[i]:
                    res.append(words[j])
                    break
        return res
sol = Solution()
print(sol.stringMatching(words1))   #['hero', 'as']
print(sol.stringMatching(words2))   #['et', 'code']
print(sol.stringMatching(words3))   #[]
print(sol.stringMatching(words4))   #['leetcode', 'od', 'am']







