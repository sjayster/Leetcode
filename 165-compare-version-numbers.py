"""
Solution:

1. One version may be longer than the other
2. Split the versions using '.' and store it in ver1 and ver2 as integers
3. We need to iterate over the longer list and when the shorter list goes out of bound, we need to pad it with 0
4. Iterate over max of len(ver1) and len(ver2)
5. Store v1 and v2 with ver1[i] and ver2[i]. 
6. If i is larger than the length of v1 or v2, instead of ver1[i] or ver2[i], we substitute 0
7. If v1 > v2, return 1
8. If v2 > v1, return -1
9. Once the loop breaks, we know the versions match, return 0

"""


class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = [int(v) for v in version1.split('.')]
        ver2 = [int(v) for v in version2.split('.')]

        lv1 = len(ver1)
        lv2 = len(ver2)
        for i in range(max(lv1, lv2)):
            v1 = ver1[i] if i < lv1 else 0
            v2 = ver2[i] if i < lv2 else 0

            if v1 < v2:
                return -1

            elif v1 > v2:
                return 1
        return 0
