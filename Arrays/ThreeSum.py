



#Two pointers
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            beg, end = i+1, len(nums)-1
            while beg < end:
                sum = nums[i] + nums[beg] + nums[end]
                if sum < 0:
                    beg += 1
                elif sum > 0:
                    end -= 1
                else:
                    result.append((nums[i],nums[beg],nums[end]))
                    while beg < end and nums[beg] == nums[beg+1]:
                        beg += 1
                    while beg < end and nums[end] == nums[end-1]:
                        end -= 1
                    beg += 1
                    end -= 1
        return result



nums = [-1,0,1,2,-1,-4]



output = Solution()
#nums = [0,0,0,0]
print(output.threeSum(nums))

