'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Author: Imanol López
Time Complexity: O(n)
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        saved_sum = nums[0]
        current_sum = 0
        
        if max(nums) < 0:
            return max(nums)

        for i in range(0, len(nums), 1):  
            current_sum += nums[i]   
            
            if current_sum > saved_sum:
                saved_sum = current_sum
                
            if current_sum < 0 :
                current_sum = 0
                
        return saved_sum