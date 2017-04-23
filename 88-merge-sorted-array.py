"""
Solution: Traverse from reverse order

1. We know that the size of nums1 is m+n.
2. While both m and n are not 0,
   a. if nums1[m-1] < nums2[n-1], set nums1[m+n-1] as nums2[n-1], decrement n
   b. else, set nums1[m+n-1] as nums1[m-1], decrement m
   
3. Once the loop breaks, if m ends before n, the 1st few elements belong to nums2. 
Hence, set nums1[:n] to nums2[:n]
4. If n ends before m, we need not do anything as nums1 will already have those elements.

"""


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
