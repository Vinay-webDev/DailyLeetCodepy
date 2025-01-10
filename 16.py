"""10/01/25"""



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
# sol = Solution()
# print(sol.wordSubsets(words1a, words2a))  #["facebook","google","leetcode"]
# print(sol.wordSubsets(words1b, words2b))  #['apple', 'google', 'leetcode']
# print(sol.wordSubsets(words1c, words2c))  #[]  ❌WRONG ANSWER❌
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
words1a = ["amazon","apple","facebook","google","leetcode"]
words2a = ["e","o"]
words1b = ["amazon","apple","facebook","google","leetcode"]
words2b = ["l","e"]
words1c = ["amazon","apple","facebook","google","leetcode"]
words2c = ["lo","eo"]
class Solution:
    def wordSubsets(self, words1, words2):
        from collections import Counter, defaultdict
        count2 = defaultdict(int)
        for w in words2:
            countw = Counter(w)
            for c, cnt in countw.items():
                count2[c] = max(count2[c], cnt)
        res = []
        for w in words1:
            countw = Counter(w)
            flag = True
            for c, cnt in count2.items():
                if countw[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res
sol = Solution()
print(sol.wordSubsets(words1a, words2a))  #["facebook","google","leetcode"]
print(sol.wordSubsets(words1b, words2b))  #['apple', 'google', 'leetcode']
print(sol.wordSubsets(words1c, words2c))  #['google', 'leetcode']  

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Solution:
    def wordSubsets(self, words1, words2):
        from collections import Counter
        req = Counter()
        for word in words2:
            cur = Counter(word)
            for ch in cur:
                req[ch] = max(req[ch], cur[ch])
        
        ans = []
        for word in words1:
            cur = Counter(word)
            if all(cur[ch] >= req[ch] for ch in req):
                ans.append(word)
        
        return ans
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""from editorials"""
"""Solution
Approach 1: Reduce to Single Word in B
Intuition

If b is a subset of a, then say a is a superset of b. Also, say N 
"a"
​(word) is the count of the number of "a"'s in the word.
When we check whether a word wordA in A is a superset of wordB, we are individually checking the counts of letters: that for each letter, we have N 
letter
​(wordA)≥N 
letter
​(wordB).
Now, if we check whether a word wordA is a superset of all words wordB 
i
​, we will check for each letter and each i, that N 
letter
​(wordA)≥N 
letter
​(wordB 
i). This is the same as checking N 
letter
​(wordA)≥ 
i
max
​
 (N 
letter
​
 (wordB 
i
​
 )).

For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.

Algorithm

Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and bmax."""

class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans













