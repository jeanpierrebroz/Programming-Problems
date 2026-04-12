from typing import List
import unittest


def search(nums: List[int], target: int) -> bool:
    if not nums:
        return False
        
    
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left // 2)
        
        if nums[mid] == target:
            return True
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return False
    

class BinarySearchTests(unittest.TestCase):
    
    def test_empty_list_returns_false(self):
        self.assertFalse(search([], 1))
        
    def test_list_size_one_returns_true(self):
        self.assertTrue(search([1], 1))
        
    def test_normal_list_returns_true(self):
        self.assertTrue(search([1, 2, 3, 4, 5], 1))
        
if __name__ == '__main__':
    unittest.main()