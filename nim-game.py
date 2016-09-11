"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

The strategy is to build a table with the number of stones and win/lose output as the resulting value.
Comparison will be done against the number of moves/stones that has been given
Say there are 12 stones. It is given that we can pick up to 3 stones. So, we will win if the number of stones is <= 3
For the 4th stone, subtract 4 with the possible moves and look up the result -> [4-1], [4-2] and [4-3]. If all the result have win in it, that means we will lose the game no matter what move we make (since we are starting the game).


stones: 1 2 3 4 5 6 7 8 9 10 11 12
result: w w w L w w w L w  w  w  L

from the above table it is clear that all multiples of 4 would result in a defeat. Hence the expression stones % 4

"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True