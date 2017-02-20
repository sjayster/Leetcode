"""
Solution 1:
1. Initialize a result array
2. for element in nums1,
   locate the index of the number in nums2 array
3. Iterate over nums2 from index to end and if number is greater than element in nums1, append it to the result array and break
4. else, append -1 to the result

This can be accomplished using a flag variable or using for.. else.. statement

Solution 2:
https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
Using a stack to store elements in nums2

1. Have a dictionary with num1 as key and index i as value. 
2. Create a result array with all [-1]
3. Iterate over the num2 array and while stack is not empty or stack[-1] is lesser than element in num2,
   pop the stack and if it is present in the dictionary, result[dictionary[stack.pop()]] = element
4. append the element to the stack
5. return the stack

"""


class Solution(object):

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        Solution 1:
        
        result = []
        length = len(nums2)
        for elt1 in nums1:
            pos = nums2.index(elt1)
            found = False
            for i in range(pos, length):
                if nums2[i] > elt1:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result

        """
        # Solution 2:

        stack = []
        result = [-1] * len(nums1)
        dict = {}
        i = 0
        for num in nums1:
            dict[num] = i
            i += 1
        for num in nums2:
            while stack and stack[-1] < num:
                top = stack.pop()
                if top in dict:
                    result[dict[top]] = num
            stack.append(num)
        return result
