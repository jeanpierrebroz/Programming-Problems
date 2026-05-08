class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(31, -1, -1):
            op = 2 ** i
            if op & n == op:
                result += 1
        
        return result