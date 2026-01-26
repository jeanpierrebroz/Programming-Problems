class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #O(n) time, O(1) space
        current = max_altitude = 0

        for num in gain:
            current+=num
            max_altitude = max(max_altitude, current)

        return max_altitude