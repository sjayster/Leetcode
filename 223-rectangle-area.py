"""
Calculate area of rect A + area of rect B - overlapping area

ABCD belong to rect A and EFGH belong to rect B.

Area of rect A = (C-A)*(D-B)
Area of rect B = (G-E)*(H-F) 
To get the intersection co-ordinates, say I1, I2, I3, I4, where I1 is the origin and I2 is on the horizontal plane of x axis, I3 is the height from I2 and I4 is the height from I1
I1->I2 = width
I2->I3 = height
I1x = max(A,E)
I1y = max(B,F)
I3x = min(C,G)
I3y = min(D,H)
result = area(rect1) + area(rect2) - area(overlap)
result = (C-A)*(D-B) + (G-E)*(H-F) - (I3x-I1x)*(I3y-I1y)

But this failed when the rectangles did not overlap.
So, we compare after computing I3x, we set I3x =  max(I1x, I3x)
and I3y = max(I1y, I3y)
If there is no intersection, the area of overlap would equate to 0
"""


class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        I1x = max(A, E)
        I1y = max(B, F)
        I3x = min(C, G)
        I3x = max(I1x, I3x)
        I3y = min(D, H)
        I3y = max(I1y, I3y)

        return (C - A) * (D - B) + (G - E) * (H - F) - (I3x - I1x) * (I3y - I1y)
