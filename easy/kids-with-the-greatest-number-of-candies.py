class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)

        for candyCount in candies:
            result.append(candyCount+extraCandies >= maxCandies)
        return result