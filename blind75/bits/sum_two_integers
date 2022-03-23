'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

Author = Imanol López
Time Complexity: O(n)
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if b > 0:
            while b > 0:
                a = a + 1
                b = b - 1
        if b < 0:
            while b < 0:
                a = a - 1
                b = b + 1

        return a