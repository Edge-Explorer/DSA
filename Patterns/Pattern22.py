# Pattern 22

# Given an integer n. 
# You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5

# Print the pattern in the function given to you.

# Solution:

class Solution:
    def pattern22(self, n):
        for i in range(2*n-2):
            for j in range(2*n-2):
                top=i
                left=j
                down= (2*n-2)-i
                right= (2*n-2)-j
                mindist= min(top, left, down, right)
                print(n-mindist, end=" ")
            print()