"""
Leetcode 252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
Input: [[0,30],[5,10],[15,20]]
Output: false
Input: [[7,10],[2,4]]
Output: true
"""
class Solution:
    def canttendMeetings(self, intervals):
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True




intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
#intervals = [[5,8],[6,8]]
#intervals = [[9,10],[4,9],[4,17]]
#intervals = [[13,15],[1,13]]
#intervals = [[9,14],[5,6],[3,5],[12,19]]

obj = Solution()
print(obj.canttendMeetings(intervals))