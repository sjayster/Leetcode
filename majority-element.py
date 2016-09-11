"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Solutions:

1. Dictionary
Create a dict with number as key and count as value
Store the max(d.values()) in a var
Iterate over the dict and return the key, if d[key] == max(d.values())

2. Using count keyword - but this would lead to time limit exceeded error if the array is really huge

3. No extra space 0(n) time 
Have 2 variables, major and count = 0.
Iterate over the list. We know that majority element will be present more than 50% times in the array.
If count == 0, then set majority element as current num
else if count >0 and if current num != majority element, decrement count
else, increment count

4. Got few more ideas from here:
https://discuss.leetcode.com/topic/17446/6-suggested-solutions-in-c-with-explanations/2

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        for num in nums:
            if not count:
                major = num
                count += 1
                
            elif count > 0 and num != major:
                count -= 1
            
            else:
                count += 1
        
        return major
        
        
        """
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        count = max(d.values())
        for k,v in d.items():
            if d[k] == count:
                return k
        """
        
        """        
        # Solution 2

        for num in nums:
            if nums.count(num) > len(nums)/2:
                return num
        """