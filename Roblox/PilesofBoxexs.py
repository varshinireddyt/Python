from collections import Counter

def pilesOfBoxes(boxesInPiles):
    cnt = Counter(boxesInPiles)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans
