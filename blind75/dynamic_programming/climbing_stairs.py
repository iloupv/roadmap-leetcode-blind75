'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

Author: Imanol López
Time Complexity: O(n)
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        i = 3
        ways_pre_pre = 1
        ways_pre = 2
   
        while(i <= n):
            
            ways = ways_pre_pre + ways_pre
            ways_pre_pre = ways_pre
            ways_pre = ways
            
            i += 1
        
        return ways