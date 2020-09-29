"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7] = [7,1,
Output: 49

Two pointer Solution
"""

def maxArea(height):

    if len(height) == 2:
        return min(height)

    maxarea = 0
    # for i in range(len(height)):
    #     for j in range(i+1,len(height)):
    #         maxarea = max(maxarea,min(height[i],height[j])*(j-i))
    # return maxarea
    i = 0
    end = len(height)-1
    while i <= end:
        maxarea = max(maxarea, min(height[i], height[end]) * (end - i))
        if height[i] < height[end]:
            i += 1
        else:
            end -=1
    return maxarea
height = [1,8,6,2,5,4,8,3,7]
#height = [1,2,1]
print(maxArea(height))
