"""
Solution 1:

1. Get the length of the string.
2. Traverse from the end of the string
3. If s[i] is not a space, increment count and set the flag to True
4. If not, check if the flag is True, if so return the count
5. If not, it is still a white space, so continue
6. Finally, return count

Solution 2: Using split()
1. split the words
2. if the list is empty, return 0 else return the length of the last element in the list.

Solution 3: 
1. Get the length of the string
2. while i>0 and s[i] is space, keep decrementing the index
3. while i>0 and s[i] is not space, increment the count and decrement the index
4. return count

"""


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        # Solution 1:
        
        length = len(s)
        count = 0
        flag = False
        for i in range(length-1,-1,-1):
            if s[i] != ' ':
                count += 1
                flag = True
            else:
                if flag:
                    return count
                    
        return count
        """

        """
        # Solution 2:
        
        a = s.split()
        if not a:
            return 0
        return len(a[-1])
        """

        # Solution 3:

        count = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
