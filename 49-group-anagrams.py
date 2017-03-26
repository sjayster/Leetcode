"""
Solution: Hash table + sort

1. We create an empty dictionary
2. Iterate over the sorted list -> ['ate', 'bat', 'eat', 'nat', 'tan', 'tea']
3. Separate the strings into characters and generate a tuple, which would be the key to our dictionary. 
When we issue sorted(list[0]), we will get 'a', 'e', 't' for ate, tea and eat.
So by creating a tuple of sorted element, we will get the same key for all the anagrams in the list
4. If d[key] is not present, d[key] = [] + [current word] -> this will create a nested list
Simple way to do it in python d[key] = d.get(key, []) + [word] => if d[key] is not present, create an empty list and append the current word as a list
If d[key] is present, get the value of d[key] and append [word] to it.
d.get(key, default -> value to return if key is not present)
5. return the values in the dictionary

"""


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in sorted(strs):
            key = tuple(sorted(word))
            d[key] = d.get(key, []) + [word]
            # If d[key] is empty, we create an empty list and then add the current word as a list (nested list)
            # If d[key] is present, we just append this word to the existing
            # list

        return d.values()
