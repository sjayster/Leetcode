"""
To find if a collision takes place between two rectangles, the following conditions must be True

1. Right side of A >= left side of B (R1.y + R1.height >= R2.y) (vertical)
2. Left side of A <= right side of B (R1.y <= R2.height + R2.y)
3. Top side of A >= bottom side of B (R1.x + R1.width >= R2.x) (horizontal)
4. Bottom side of A <= top side of B (R1.x <= R2.width + R2.x)

If we happen to include the origin coordinates - Instead of (0,0), if the user wants to specify something else, we should account for that too.

"""


class Solution(object):

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def intersect(cls, rect1, rect2):
        if (rect1.x + rect1.width >= rect2.x) and (rect1.x <= rect2.x + rect2.width) and (rect1.y + rect1.height >= rect2.y) and (rect1.y <= rect2.y + rect1.height):
            return True

        return False

rect1 = Solution(0, 0, 5, 5)
rect2 = Solution(0, 0, 5, 5)
print Solution.intersect(rect1, rect2)

rect3 = Solution(0, 0, 6, 7)
rect4 = Solution(0, 8, 4, 5)
print Solution.intersect(rect3, rect4)

rect5 = Solution(1, 4, 4, 7)
rect6 = Solution(7, 3, 8, 4)
print Solution.intersect(rect5, rect6)

"""
OUTPUT:

True
False
"""
