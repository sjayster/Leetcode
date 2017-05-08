"""
Solution:

a. Simplest: Sort and return arr[-k]
b. Use heap (max heap)
1. Dump all the elements in a heap (I used min heap)
2. Iterate over range(len(arr)-k+1)
3. Keep popping one element at a time
4. Once the loop breaks, we have the answer
"""


class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        heapq.heapify(nums)
        l = len(nums)
        for i in range(l - k + 1):
            ans = heapq.heappop(nums)

        return ans

        """
        return sorted(nums)[-k]
        """
