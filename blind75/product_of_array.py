
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Author: Imanol López
Time Complexity: O(2*n)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        # Edge Cases
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        products = [1] * (len(nums))
        
        p = nums[0]
        products[0] = 1
        
        # Left
        for i in range(1, len(nums), 1):   
            products[i] = p
            p = nums[i] * p
            
        # Right
        p = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] = p * products[i]    
            p = nums[i] * p
        
        return products