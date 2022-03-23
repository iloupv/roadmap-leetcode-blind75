/*
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

Author = Imanol López
Time Complexity: O(n)
*/
class Solution {
public:
    int getSum(int a, int b) {
        int carry;
        carry = 0;
        while(b != 0)
        {
            carry = (a & b); // Get same bits (AND).
            a = (a ^ b); // XOR operation, to get the sum without carry.
            b = (carry) << 1; // Bit shift <<, add the carry for the next iteration.
        }
        return a;
    }
};