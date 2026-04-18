class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        
        a = ""
        minlen = min(len1, len2)
        
        for i in range(minlen):
            a = a + word1[i]
            a = a + word2[i]
        
        if len1 > len2:
            a = a + word1[minlen:]
        elif len1 < len2:
            a = a + word2[minlen:]

        return a