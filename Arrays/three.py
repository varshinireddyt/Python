def threeSum(nums):
    output = []
    dict = {}
    three_sum = []
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            diff = -(nums[i] + nums[j])
            if diff in dict and dict[diff] != i and dict[diff] != j:
                three_sum = [nums[i],nums[j],diff]
                #three_sum.sort()
            if three_sum not in output:
                output.append(three_sum)
    return output





nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


