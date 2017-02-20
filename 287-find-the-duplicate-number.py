"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

Solutions that I could think of.
1. Using a dictionary to save the 1st occurrence of the number. If the num is seen again, return

2. Sort the array and then compare if nums[i] == nums[i-1]
Example: nums = [5,2,3,1,2,4]
nums.sort() -> [1,2,2,3,4,5]
if nums[i]==nums[i-1], return nums[i]

3. Using linked list cycle example, we can have slow and fast pointers to find the duplicate
a. if number of elements > 1, set slow = a[0] and fast = a[a[0]]
b. while slow != fast, do slow = nums[slow] and fast = nums[nums[fast]]
c. Once it matches, set fast to 0 (iterate fast from beginning) and move one step at a time until a match is found.
d. return slow/fast as that points to the value, else return -1
"""


class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Solution 1:
        
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return num
        """
        """
        Solution 2:
        
        length = len(nums)
        nums.sort()
        if length > 1:
            for i in xrange(length):
                if nums[i] == nums[i-1]:
                    return nums[i]
        """
        """
        Solution 3:
        """
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow

        return -1
