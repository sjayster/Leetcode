"""
2 solutions:
1. Using hash tables - straight forward solution
If element is not in the dict, add it, else return True. Finally return False

2. Python trick:
get the length of the nums array
convert the array to a set - this will remove all the dup elements.
Now get the length of the set. If the length(nums) equals length(set) then there are no dups - return False
If there are dups, set will be lesser than the list. return (length(set) < length(nums)) - return True 

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return True
        
        return False
        """
        
        return (len(set(nums)) < len(nums))
        