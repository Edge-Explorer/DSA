# Pattern 19

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern19(self, n):
        inis=0
        for i in range(n):
            print("*" * (n-i), end="")
            print(" " * inis, end="")
            print("*" * (n-i))
            
            inis +=2
        
        inis=2*n-2
        for i in range(1, n+1):
            print("*" * i, end="")
            print(" " * inis, end="")
            print("*" * i)
            
            inis -=2