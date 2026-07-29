# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:



# *

# **

# ***

# ****

# *****

# ****

# ***

# **

# *



# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern10(self, n):
        
        # Upper Part
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
        
        # Lower Part
        for i in range(1, n):
            for j in range(n, i, -1):
                print("*", end="")
            print()