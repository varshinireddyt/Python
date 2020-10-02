class Solution:
    def threeSum(self, nums):
        out = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(len(nums)-1, j, -1):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        res = [nums[i],nums[j],nums[k]]
                        res.sort()
                        out.append(res)
        # # result = []
        # import copy
        # result = copy.deepcopy(out)
        # if len(out) == 1 :
        #     return out
        # else:
        #     for m in range(len(out)):
        #         for n in range(m + 1, len(out)):
        #             if out[m] == out[n]:
        #                 print(n)
        #                 del result[m]
        #
        #                 if len(out) == 1 :
        #                     return result

        result = []

        for i in range(len(out)):
            if (result.__contains__(out[i])):
                print()
            else :
                result.append(out[i])

        return result

nums = [-1,0,1,2,-1,-4]



output = Solution()
#nums = [0,0,0,0]
print(output.threeSum(nums))

