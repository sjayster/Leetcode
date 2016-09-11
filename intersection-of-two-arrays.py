"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

Solution - hashmap:
Iterate over one of the arrays and add it to a hash table.
Create an empty result to store the result
Iterate over 2nd list. If the element is present in the hash table and not in result, append it to result.

Good reference for other types of solution:
https://discuss.leetcode.com/topic/45727/four-python-solutions-with-simple-explanation/2
Converting the lists to set and performing "AND" seems to be the fastest solution
"""

class Solution(object):
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        d = {}
        
        for num in nums1:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for num in nums2:
            if num in d and num not in result:
                result.append(num)
        
        return result

"""
return list(set(nums1) & set(nums2))
"""