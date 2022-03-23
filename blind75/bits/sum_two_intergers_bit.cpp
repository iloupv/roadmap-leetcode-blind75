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