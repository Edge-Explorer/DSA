# You are given an integer n. 
# Return the integer formed by placing the digits of n in reverse order.

# Example 1

# Input: n = 25

# Output: 52

# Explanation: Reverse of 25 is 52.

# Example 2

# Input: n = 123

# Output: 321

# Explanation: Reverse of 123 is 321.

# Solution:

class Solution:
    def reverseNumber(self, n):
        a=int(str(n)[::-1])
        return a
    

# Optimized Approach 

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        
        if x<0:
            rev= int(str(x)[1:][::-1])*-1
        else:
            rev= int(str(x)[::-1])
        
        if rev>2 **31-1 or rev<-2 ** 31:
            return 0
        
        return rev