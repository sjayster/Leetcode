"""
Solutions: Both using sets

1. Create 3 sets, row1, row2 and row3 with the chars in that row
2. Iterate over the words and form sets of the word, so that the dups are removed.
3. Check if wordset is a subset of the row set. If so, append the word to the result
4. Alternatively, we can also AND the wordset with the row set to see if the word set is returned back.
"""


class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        for word in words:
            w = set(word.lower())
            if w.issubset(row1):
                result.append(word)
            if w.issubset(row2):
                result.append(word)
            if w.issubset(row3):
                result.append(word)

        return result

        """
        Solution 2:

        result = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        for word in words:
            w = set(word.lower())
            if w & row1 == w:
                result.append(word)
            if w & row2 == w:
                result.append(word)
            if w & row3 == w:
                result.append(word)
                
        return result
        """
