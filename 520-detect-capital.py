"""
Solution 1:

Get the number of upper case characters in the string - Upper case ord is between 65 to 96
1. If number of upper case = len(string) or if the count is 0, return True
2. Else if the count is 1, check if the first character is the upper case char, if not return True
3. else, return false

Solution 2:
Pythonically, we can just return if string is upper or lower or title
"""


class Solution(object):

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Solution 1

        count = 0
        for char in word:
            if 65 <= ord(char) < 96:
                count += 1

        if count == len(word) or count == 0:
            return True
        elif count == 1:
            return ord(word[0]) < 96
        else:
            return False
        """

        # Solution 2:

        return word.isupper() or word.islower() or word.istitle()
        """
