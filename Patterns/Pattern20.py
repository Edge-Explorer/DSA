# Pattern 20

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern20(self, n):
        init_spaces=2*n-2
        
        for i in range(1, 2*n):
            stars= i
            
            if i>n:
                stars= 2*n-i
                
            print("*" * stars, end="")
            print(" " * init_spaces, end="")
            print("*" * stars)
            
            if i<n:
                init_spaces -=2
            else:
                init_spaces +=2