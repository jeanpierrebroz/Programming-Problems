class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        for i, digit in enumerate(digits):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0
        
        if digits[-1] == 0:
            digits.append(1)

        digits.reverse()
        return digits