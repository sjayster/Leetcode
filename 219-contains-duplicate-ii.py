"""
Solution:

1. Create an empty dict
2. Enumerate over the list and store the element as the key and index as the value, if element not in d
3. If element in d, check if index - d[element] < k, return True
4. Once the loop breaks, return False

"""


class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i

        return False
