"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Solution: Use a hash map/dictionary

Since we have no restriction like the number must be seen only once, we can skip that step.
Iterate over list 1 with element as key and occurrence as the value.

Iterate over list 2 and if the element is seen, decrement the count by 1 and add the key to the list, if count >0
Return the list
"""

class Solution(object):
    def intersect(self, nums1, nums2):
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
            if num in d and d[num] > 0:
                result.append(num)
                d[num] -= 1
        
        return result