# Pattern 17

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern17(self, n):
        for i in range(n):
            
            # Print leading spaces
            print(" " * (n - i - 1), end="")
            
            # Initialize character to start from 'A'
            ch = ord('A')
            breakpoint = (2 * i + 1) // 2
            
            # Print characters in row
            for j in range(1, 2 * i + 2):
                print(chr(ch), end="")
                if j <= breakpoint:
                    ch += 1
                else:
                    ch -= 1

            print()