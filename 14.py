"""08/01/25"""
words1 = ["a","aba","ababa","aa"]
words2 = ["pa","papa","ma","mama"]
words3 = ["abab","ab"]
words4 = ["a","abb"]
class Solution:
    def countPrefixSuffixPairs(self, words):
        N = len(words)
        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                str1 = words[i]
                length = len(str1)
                str2 = words[j]
                if str1 == str2[:length] and str1 == str2[-length:]:
                    count += 1
        return count
sol = Solution()
print(sol.countPrefixSuffixPairs(words1))   #4
print(sol.countPrefixSuffixPairs(words2))   #2
print(sol.countPrefixSuffixPairs(words3))   #0
print(sol.countPrefixSuffixPairs(words4))   #0





