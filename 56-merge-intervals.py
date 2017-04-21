"""
Solution: Sort and compare - pretty straightforward
NOTE: The input is a list of tuples. 
For sorting the tuple, we need to make use of sorted()
To sort the tuple by the start value, we use the key attr in the sorted()

1. Sort the list with x.start as the key
2. Add the 1st interval to the result array
3. Traverse from the 2nd interval to the end of the interval array and do the following,
    a. If the current.start is <= result[-1].end, we know that the list is overlapping
    example: result has [[1,3],[7-10]] and currently we are in [9-12]
    Compare result[-1].end, which is 10, with current.start, which is 9 => overlapping
    
    b. But we need to determine what the result.end must be. If result[-1].end > current.end, we can leave it as is, else result[-1].end will be current.end. 
    Example: res = [7,15] curr = [9-12]. Here start and end will not change for result
    Example: res = [7,10] curr = [9-12]. Here result.end will become 12
    Hence, result[-1].end = max(curr.end, result[-1].end)
4. Return result

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]

        for i in intervals[1:]:
            if i.start <= result[-1].end:
                result[-1].end = max(i.end, result[-1].end)
            else:
                result.append(i)
        return result
