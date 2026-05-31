class NumArray:

    def __init__(self, nums: List[int]):
        self.numarray = [0]
        counter = 0
        for num in nums:
            counter += num
            self.numarray.append(counter)

    def sumRange(self, left: int, right: int) -> int:
        
        return self.numarray[right + 1] - self.numarray[left]