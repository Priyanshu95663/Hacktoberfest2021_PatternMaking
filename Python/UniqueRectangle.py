# Unique Rectangle Problem Statement
# You are given N unit squares (squares with side length 1 unit), and you are asked to make rectangles using these squares.
# You have to count the number of rotationally unique rectangles than you can make.
# What does rotationally unique mean? Well, two rectangles are rotationally unique if one can’t be rotated to become equivalent to the other one.

# Example:
# The 4×2 rectangle can be rotated 90 degrees clockwise to make it the exact same as the 2×4 rectangle and so these are not rotationally unique.

def count_unique_rectangle(n):
    count=0
    for i in range(1, int(n**0.5) +1):
        height = i
        while (height*i) <=n:
            count +=1
            height+=1
    return count

print(count_unique_rectangle(int(input())))