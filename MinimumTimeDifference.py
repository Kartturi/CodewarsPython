# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# 2.The input time is legal and ranges from 00:00 to 23:59.

input = ["23:59", "00:00"]


class Solution:
    def findMinDifference(self, timePoints) -> int:
        point1 = timePoints[0]
        point2 = timePoints[1]
        point1_inputs = point1.split(":")
        point1_minutes = (int(point1_inputs[0]) * 60) + int(point1_inputs[1])

        point2_inputs = point2.split(":")
        point2_minutes = (int(point2_inputs[0]) * 60) + int(point2_inputs[1])

        sorted_list = [point1_minutes, point2_minutes]
        sorted_list.sort(reverse=True)
        option1 = sorted_list[0] - sorted_list[1]
        option2 = 1440 + sorted_list[1] - sorted_list[0]

        return option1 if option1 < option2 else option2


sol = Solution()
result = sol.findMinDifference(input)
print(result)
