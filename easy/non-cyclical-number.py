class Solution:
    def isHappy(self, n: int) -> bool:

        def returnSquares(num):
            res = 0
            num = str(num)
            for number in num:
                res += int(number) ** 2
            return res
        
        processed = set()
        happy = returnSquares(n)

        while happy not in processed:
            processed.add(happy)
            happy = returnSquares(happy)
        
        return happy == 1