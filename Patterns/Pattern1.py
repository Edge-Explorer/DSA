# Pattern 1

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

# *****

# *****

# *****

# *****

# *****

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern1(self, n):
        for i in range(0, n):
            print("*" * n)