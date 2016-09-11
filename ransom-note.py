""" 
 Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

Used hashmap (dictionary) to solve this problem
Create a dictionary d and store the occurrence of all the characters in the magazine
In the second for loop, iterate over the ransomNote and see if the characters are present in the dictionary, if so decrement the count by 1. 
If the count reaches 0 and still a character appears, return False
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        d = {}
        count = 1
        for i in magazine:
            if i not in d:
                d[i] = count
            else:
                d[i] += 1
        
        for i in ransomNote:
            if i in d and d[i] > 0:
                d[i] -= 1
            else:
                return False
        
        return True