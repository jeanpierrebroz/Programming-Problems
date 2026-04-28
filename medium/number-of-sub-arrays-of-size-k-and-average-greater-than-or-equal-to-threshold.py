class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        s = 0
        result = 0

        for r, num in enumerate(arr):
            s += num

            if r - l + 1 > k:
                s -= arr[l]
                l += 1
            
            if r - l + 1 == k:
                avg = s / k
                if avg >= threshold:
                    result+=1
        
        return result