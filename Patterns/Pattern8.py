# Pattern 8

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:



#*********
# *******
#  *****
#   ***
#    *


# Print the pattern in the function given to you.

# Solution 1:

class Solution:
    def pattern8(self, n):
        for i in range(n):

            for j in range(i):
                print(" ", end="")
        
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")

            for j in range(i):
                print(" ", end="")

            print()

# Solution 2:

class Solution:
    def pattern8(self, n):
        for i in range(n):

            for j in range(i):
                print(" ", end="")
        
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")
                
            print()