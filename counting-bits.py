"""
2 solutions: bit manipulation and DP

Iterative:
 We need to iterate to num+1 as the last digit is also included
 If we & num with num-1, it will take number of 1's in a num times before it reaches 0
 Example: num = 15 = 1111, count = 0
 while num != 0: num & (num-1); count += 1
 1111 & 1110 = 1110
 1110 & 1101 = 1100
 1100 & 1011 = 1000
 1000 & 0111 = 0
 It takes 4 steps (number of 1's in the number) for num to reach 0

DP:
https://discuss.leetcode.com/topic/43202/easy-understanding-dp-bit-java-solution
Didn't know how DP worked. Had to see some examples to see how it worked for this problem.
When nums is 9, the ans is [0,1,1,2,1,2,2,3,1,2]

We know result[0] = 0 and can hard set it.
result[1] = result[1&0] + 1
We will see what happens for result[9]
result[9] = result[9&8] + 1 = result[8] + 1 = 1+1 = 2

result[15] = result[15&14] +1 = result[14]+1 = 3+1 = 4

UPDATE: In one of the threads they had mentioned that append/insert takes a lot of time. Hence allocate nums+1 times [0]


"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # Iterative:
        
        result = []
        for i in range(num+1):
            count = 0
            while i != 0:
                i &= i-1
                count += 1
                
            result.append(count)
            count = 0
        
        return result
        
        """
        # DP - Sol 1
        
        result = []
        result.append(0)
        
        for i in xrange(1,num+1):
            result.insert(i, result[i&(i-1)] +1)
            
        return result
        
        # Updated Solution with - no insert or append
        
        result = [0] * (num+1)
        for i in xrange(1, num+1):
            result[i] = result[i&(i-1)] + 1
            
        return result
        """