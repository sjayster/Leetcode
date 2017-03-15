"""
Solution:
1. Calculate the number of words based on whitespace characters.
2. Pretty simple in python, split() splits the string based off spaces and generates a list.
3. Return the length of the list.

For interview purposes:

1. Get the length of the string
2. Initialize a count var to 0 and flag variable to False (This will be reassigned when we encounter space)
3. Iterate over the length and if the char is not a space and the flag is set to True, increment the count and set flag to True - by doing this, we will keep moving on until we see a white space
4. In the else, condition, if we happen to see a white space, we will reset the flag as False
5. Whenever we see a white space the flag will be set to false, so even if there is a barrage of white spaces, we are good.
6. Whenever we see a non space char, we will check if the flag is set, if not, we can increment the count. 
"""


class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Solution 1:
        return len(s.split())

        """
        Solution 2:
                count = 0
        length = len(s)
        flag = False
        for i in range(length):
            if s[i]!=' ' and not flag:
                count += 1
                flag = True
            else:
                if s[i] == ' ':
                    flag = False

        return count
        """
