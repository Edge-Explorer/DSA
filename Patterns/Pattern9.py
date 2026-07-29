# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:



#    * 
#   ***
#  *****
# *******
#*********
#*********
# *******
#  *****
#   ***
#    *


# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern9(self, n):
        # Top
        for i in range(n):
            for j in range(n -i -1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()
        
        # Bottom
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")
            print()