class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        prefix = ""

        for i in range(0, len(words)):
            if (words[i][0] == searchWord[0]):
                prefix = words[i][:len(searchWord)]
                if (prefix == searchWord):
                    return i+1
        
        return -1