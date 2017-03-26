"""
Solutions:

I was able to think of 3 different solutions

Solution 1:
Simple while loop
We know we will have to check from 1 to num/2 + 1 to see if the num is a square or not.
1. initialize i to 1
2. while i^2 < num, set i to i+1
3. Once the loop breaks, we check to see if i^2 == num, if so return True
4. else, return False


Solution 2:
Binary search

1. Set start to 1 and end to num/2 + 1
2. while start <= end, get the mid point
3. if mid^2 == num, return True
4. if mid^2 > num, set end to mid -1
5. if mid^2 < num, set start to mid + 1

Solution 3:
Recursion - Similar to BS
1. Set start to 1 and end to num/2 + 1
2. Call binarysearch(start, end, num)
3. Same logic as BS, but recurse over binarysearch instead of while loop

"""


class Solution(object):

    # Solution 1
    def isPerfectSquare(self, num):
        mid = 1
        while mid * mid < num:
            mid += 1

        if mid * mid == num:
            return True

        else:
            return False
    """        
    # Solution 2
    def isPerfectSquare(self, num):
        if num == 1:
            return True
            
        start = 1
        end = (num/2) + 1
        while start <= end:
            mid = (start + end)/2
            
            if mid * mid == num:
                return True
                
            if mid *mid > num:
                end = mid - 1
                
            else:
                start = mid + 1
        
        return False
    """
    """
    # Solution 3           
    def binarysearch(self, start, end, num):
        if start < end:
            mid = (start + end)/2
            if mid*mid == num:
                return True
            
            if mid*mid < num:
                return self.binarysearch(mid+1, end, num)
                
            if mid*mid > num:
                return self.binarysearch(start, mid, num)
        
        return False
        
    
    def isPerfectSquare(self, num):
        start = 1
        if num == 1:
            return True
        return self.binarysearch(start, (num/2)+1, num)
    """
