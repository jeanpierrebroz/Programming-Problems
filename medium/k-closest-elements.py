class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if k == len(arr):
        #     return arr
        


        # curr = sum(abs(v - x) for v in arr[:k])
        # best = curr
        # start_index = 0

        # for l in range(1, len(arr) - k + 1):
        #     curr += -abs(arr[l-1] - x) + abs(arr[l + k - 1] - x)
        #     if curr < best:
        #         best = curr
        #         start_index = l
            
        # return arr[start_index:start_index+k]
        n = len(arr)
        if k == n:
            return arr
        
        l, r = 0, n - k

        while l < r:
            mid = (l + r) // 2
            
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
            
        return arr[l:l + k]