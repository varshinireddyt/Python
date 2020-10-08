"""
39. Combination Sum:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

"""
#using backtrack solution
#Time Complexity: O(N ** (T/M + 1)),  N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
class Solution(object):
    def combinationSum(self, candidates, target):
        output = []
        def backtrack(remain, next_candidate, start):
            if remain < 0:
                return
            elif remain == 0:
                output.append(list(next_candidate))
                return
            else:
                for i in range(start,len(candidates)):
                    next_candidate.append(candidates[i])
                    backtrack(remain-candidates[i], next_candidate, i)
                    next_candidate.pop()
        backtrack(target,[],0)
        return output

combination = Solution()
candidates = [2,3,6,7]
target = 7
print(combination.combinationSum(candidates,target))




