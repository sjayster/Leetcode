"""
Solution: Using stack and dictionary

1. Have a dictionary with closing brackets as the key and opening brackets as the value
2. Iterate over the string and whenever we see an open bracket, we add it to the stack
3. When a closed bracket, say ], is seen, we need to see if the previous element was a [
4. So, we pop the stack and lookup the dictionary to see if d[']'] == stack.pop()
5. If the stack is empty or if the above condition is False, return False.
6. If everything goes on well, the stack will be empty after all the pops.
7. return not mystack

"""


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack = []
        d = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if "{" == c or "(" == c or "[" == c:
                mystack.append(c)
            else:
                if not mystack or d[c] != mystack.pop():
                    return False
        return not mystack
