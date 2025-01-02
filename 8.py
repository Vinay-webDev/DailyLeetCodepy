"""02/01/25"""
words1 = ["aba","bcb","ece","aa","e"]
queries1 = [[0,2],[1,4],[1,1]]
words2 = ["a","e","i"]
queries2 = [[0,2],[0,1],[2,2]]
words3 = ["bzmxvzjxfddcuznspdcbwiojiqf",
          "mwguoaskvramwgiweogzulcinycosovozppl",
          "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
          "uivcdsboxnraqpokjzaayedf","yalc",
          "bbhlbmpskgxmxosft","vigplemkoni",
          "krdrlctodtmprpxwditvcps","gqjwokkskrb","bslxxpabivbvzkozzvdaykaatzrpe","qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi","siqbezhkohmgbenbkikcxmvz","ddmaireeouzcvffkcohxus","kjzguljbwsxlrd","gqzuqcljvcpmoqlnrxvzqwoyas","vadguvpsubcwbfbaviedr","nxnorutztxfnpvmukpwuraen","imgvujjeygsiymdxp","rdzkpk","cuap","qcojjumwp","pyqzshwykhtyzdwzakjejqyxbganow","cvxuskhcloxykcu","ul","axzscbjajazvbxffrydajapweci"]
class Solution:
    def vowelStrings(self, words, queries):
        vowels = ("a", "e", "i", "o", "u")
        count = 0
        res = []
        for i in range(len(queries)):
            s = queries[i][0]
            e = queries[i][1]
            for j in range(s, e + 1):
                string = words[j]
                if string[0] and string[len(string) - 1] in vowels:
                    count += 1
            res.append(count)
            count = 0
        return res
sol = Solution()
print(sol.vowelStrings(words1, queries1))   #[2, 3, 0]
print(sol.vowelStrings(words2, queries2))   #[3, 2, 1]
#❌❌WRONG ANSWER❌❌

