"""
Solution:

In Python string is immutable, so, convert the string to a list using list(s) or list comprehension [x for x in s]
1. Set a start and end index pointing to 0 and end of list
2. as long as start < end, check if s[start] has vowels, if not, increment start
3. Similarly, check if s[end] has vowels, if not, decrement end.
4. When both s[start] and s[end] have vowels, the while loop will break.
5. Swap the values at s[start] and s[end] and increment start and decrement end
6. Finally, join the list and return the result

Note:

We use while start< end in the inner conditions, when we encounter a word without vowels.
example: "try"
if the condition start< end is not present in s[start] not in "aeiouAEIOU", start will increment until it runs out of range. 

"""


class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and s[start] not in "aeiouAEIOU":
                start += 1
            while start < end and s[end] not in "aeiouAEIOU":
                end -= 1

            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

        return ''.join(s)
