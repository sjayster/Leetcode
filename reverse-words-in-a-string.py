"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Solution:
The immediate solution that I can think of was to make use of the built-in sting.split()
The split() separates words with the spaces and also removes trailing spaces.
Then return ' '.join(split_words_list)

With extra space, the runtime is close to 100% efficient
Without extra space, the code takes a bit longer. I think the reason is, in the 2nd approach, we go through the split operation for every word. Whereas in the first one, the split is a one time occurrence.

# If they don't let us use the split operation, the following solution works:

1. get the length of the string, have a flag to see if a regular char (excl space) is found, position variable to mark the start of the char (initially set it to something negative - as we need this if the string is all spaces) and an empty list
2. Iterate over the length and no matter what we will encounter the following cases:
    a. char is valid
    b. char is space
    
3. If the char is valid and the flag is set to False, set the positional var to the index of the char
   If the char encountered is a space and the flag is set to True, copy the contents of the string from positional_var to the current index to a list and set flag to False.
   If the char encountered is valid or invalid and the flag is set, keep continuing.
   
4. Two catches are what if the string ends with a valid character or if the string has all spaces.
   a. Upon exiting the for loop, check to see if the flag is set to true. If so, copy the contents from pos_var to "i+1" (including i) to the new list

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = False
        length = len(s)
        result = []
        pos = 0 #initialize to something negative
        #if length <= 1:
            #return s
        for index in xrange(length):
            if s[index] != ' ' and not flag:
                pos = index
                flag = True
            
            elif s[index] == ' ' and flag:
                result.insert(0, s[pos:index])
                flag = False
            
            else:
                continue
        
        if flag:
            result.insert(0, s[pos:index+1])
        return ' '.join(result)

        """
        Approach 1: beats 100% runtime
        
        t = s.split()
        return ' '.join(t[::-1])
        """
        
        """
        Approach 2: beats 37% runtime
        return ' '.join(s.split()[::-1])
        """
