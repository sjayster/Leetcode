"""
Solution: 2 pointers
1. Have an index initialized to 0
2. Iterate over 1 to length(nums)
3. If nums[i] == nums[index], we don't do anything
4. Else, we move index by 1 and assign nums[i] to nums[index]
The reason is, if there were duplicates, the index wasn't incremented and remained at the same position, whereas i kept increasing.
When a duplicate is not seen, we just move a[i] to a[index+1]
example:
a = [1,2,2,2,3]
i = 1, index = 0, increment index and set a[index] to a[i]. No change in the array
i = 2, index = 1, match seen, keep moving
i = 3, index = 1, match seen, keep moving
i = 4, index = 1, increment index and set a[2] to a[i] => [1,2,3,x,x]
5. return index+1 (as index+1 is the length of the new array)

"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        index = 0
        length = len(nums)
        for i in range(1, length):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]

        return index + 1
