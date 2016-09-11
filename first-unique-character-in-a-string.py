"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Solution:

1. As usual, the first method that came to my mind was to make use of a hash table.
However, I complicated it a bit and my friend suggested me approaches 2 and 3

a. Create a dictionary with "char" as key and list[count, index] as value
b. Set a result var to sys.maxint
c. Iterate over the dict and if d[k][0] (count) == 1, check if d[k][1] (index) is < result
d. If so replace the result with the index val (This will keep replacing the result var with the least index)
e. Finally, check if result is < sys.maxint, if so return result else return -1

2. Suggested change:

a. Create a dictionary with "char" as key and "count" as value
b. Iterate over the string and see if d[k] == 1, if so return the index, finally return -1 if no matches are seen

3. Using array
a. Create an array with 26 0's (1 for each alphabet)
b. Traverse over the string and replace the position of the char with the count. like "c" would be the 3rd letter -> array[2], using ord("char") - ord("a").
c. Once the list is populated, traverse through the result array and return the index if result[ord(char) - ord("a")] == 1.

4. Using Python's count(). This will run into a runtime error if the string is infinitely long.

"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        Solution 1:
        d = {}
        ans = []
        length = len(s)
        for i in range(length):
            if s[i] not in d:
                d[s[i]] = [1, i]
            else:
                d[s[i]] = [-100,i]
        
        ans = sys.maxint
        for k,v in d.items():
            if d[k][0] == 1 and d[k][1] < ans:
                ans = d[k][1]
        
        if ans < sys.maxint:
            return ans
        return -1
        """
        
        """
        Solution 2:
        
        length = len(s)
        d = {}
        for i in xrange(length):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
                
        for i in xrange(length):
            if d[s[i]] == 1:
                return i
        
        return -1
        """
        
        # Solution 3:
        
        result = [0] * 26
        length = len(s)
        for i in s:
            result[ord(i)-ord('a')] += 1
            
        for i in xrange(length):
            if result[ord(s[i])-ord('a')] == 1:
                return i
        return -1

        """
        Solution 4:
        
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        
        return -1
        """
