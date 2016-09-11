"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

CLUES: When they say the array is sorted, the solution will either be 2 pointers or binary search algorithm
My solution: Use 2 pointers i and j since the array has already been sorted
Calculate length - 0(n)
i =0 and j = length-1
if sum(num[i], num[j]) < target, we need to move i ahead as num[i] will be higher than num[i-1]
if sum(num[i], num[j]) > target, we know we need to decrease our last element and see if the target is hit
else, we can return the position of i and j as we know for sure that there is at least 1 pair in the array that would sum up to the target
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        i = 0
        j = length-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return i+1, j+1
                
"""
Solution 2: Using Dictionary

class Solution(object):
    def twoSum(self, numbers, target):
        d = {}
        length = len(numbers)
        for value, key in enumerate(numbers):
            if target-key in d:
                index1 = d[target-key]+1
                index2 = value + 1
                return index1, index2
            
            d[key] = value
        
"""