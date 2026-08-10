# You are given an integer n. 
# You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

# Example 1

# Input: n = 4

# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2

# Input: n = 14

# Output: 2

# Explanation: There are 2 digits in 14.

# Solution:

class Solution:
    def countDigit(self, n):
        last_digit=0
        while n>0:
            last_digit +=1
            n= n//10
            print(last_digit)
        return(last_digit)
    
# Optimized Approach 

import math

def countDigit(n):
    last_digit= int(math.log10(n)+1)
    return last_digit