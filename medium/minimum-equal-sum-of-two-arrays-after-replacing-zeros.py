class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #the sum of the arrays PLUS the number of 0s is the minimum both arrays have to be. 
        # if both arrays have at least one 0, then the result is the max of those 2 arrays
        # if the smaller array with this in mind doesn't have 0s, then return -1

        s1, s2 = sum(nums1), sum(nums2)
        c1, c2 = nums1.count(0), nums2.count(0

        if (c1 == c2 == 0) and s1 != s2:
            return -1

        elif c1 != 0 and c2 != 0:
            return max(s1 + c1, s2 + c2)
        
        elif s1 + c1 <= s2 and c2 == 0:
            return s2
        elif s2 + c2 <= s1 and c1 == 0:
            return s1
        else:
            return -1