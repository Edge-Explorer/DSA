# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

# 1 

# 0 1 

# 1 0 1 

# 0 1 0 1 

# 1 0 1 0 1

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern11(self, n):
        start= 1
        for i in range(n):
            if (i % 2 == 0):
                start= 1
            else:
                start= 0
            for j in range(i + 1):
                print(start , end=" ")
                start = 1 - start
            print()