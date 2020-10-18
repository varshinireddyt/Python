"""""
Leetcode 253: Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
"""

import heapq
class Solution:
    #using priority queue, time complexity: O(N log N) ---> O(N) for sorting O( log N) for extracting the min operation on a heap
    def minMeetingRooms(self, intervals):
        if not intervals:  #if no meeting then no rooms
            return 0
        #heap initialization
        free_rooms = []
        #sort the meetings based on the start time
        intervals.sort(key= lambda x: x[0])
        # add the new room to the first meeting
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1,len(intervals)):
            # assigning the free room to the next meeting and removing the previous end time
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms,intervals[i][1])
        return len(free_rooms)


#approach 2: sorting
    def minMeetingRoom(self, intervals):
        if not intervals:
            return 0
        start_time = sorted([i[0] for i in intervals]) #sorting the start time
        end_time = sorted(i[1] for i in intervals)  #sorting the end time
        N = len(intervals)
        used_rooms = 0
        start_pointer = 0
        end_pointer = 0
        while start_pointer < N:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_time[start_pointer] >= end_time[end_pointer]:
                # Free up a room and increment the end_pointer
                used_rooms -= 1
                end_pointer += 1

                # We do this irrespective of whether a room frees up or not.
                # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
                # remain the same in that case. If no room was free, then this would increase used_rooms

            used_rooms += 1
            start_pointer += 1
        return used_rooms






obj = Solution()
#intervals = [[0, 30],[5, 10],[15, 20]]
intervals = [[7,10],[2,4]]
print(obj.minMeetingRooms(intervals))