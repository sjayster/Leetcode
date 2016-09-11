"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].


Solutions:

1. Immediate solution that I could think of is by using division.
Get the product of the array and divide the product by each number.

2. Common solution:
Have a multiplier variable called prod set to 1
Multiply elements from the 1st element to last-1 element - store it in an array
Multiply the elements from the last element to the 2nd element - store it in another array
traverse through the length and multiply items from both the array and store it in a separate array -> output

sample: nums = [2,3,4,5] expected output = [60, 40, 30, 24]
vars prod1 and prod2 are set to 1

Traverse from left to right-1:
Multiply prod1 with nums[i] to nums[right-1] and store to res1 -> [1,2,6,24]
In the same loop, multiply prod2 with nums[-1-i] and store it to res2 -> [1,5,20,60]

Now traverse through the length and multiply the res1[i] and res2[-1-i] and store it to output -> [60,40,30,24]

Note:
Instead of having 2 arrays res1 and res2, we can have a single array too.
Refer: https://discuss.leetcode.com/topic/18983/python-solution-accepted-o-n-time-o-1-space 

"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prod1 = 1
        prod2 = 1
        length = len(nums)
        res1 = []
        res2 = []
        output = []
        for i in range(0,length):
            res1.append(prod1)
            res2.append(prod2)
            prod1 *= nums[i]
            prod2 *= nums[-1-i]
        
        for i in range(0, length):
            prod = res1[i]*res2[-1-i]
            output.append(prod)
        
        return output
        
        """
        prod = 1
        for i in nums:
            prod *= i
            
        output = []
        for i in nums:
            output.append(prod/i)
            
        return output
        """