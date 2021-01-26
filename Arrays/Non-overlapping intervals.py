"""
435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
"""


def eraseOverlapIntervals(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return 0
    intervals.sort(key = lambda x:x[1])
    #print(intervals)
    result = intervals[0][1]
    count = 1

    for i in range(1,len(intervals)):
        if result <= intervals[i][0]:
            result = intervals[i][1]
            count += 1

    return len(intervals) - count



#intervals = [[1,2],[2,3],[3,4],[1,3]]
#intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))