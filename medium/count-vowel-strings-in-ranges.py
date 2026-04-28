class Solution:
    def startsAndEndsWithVowel(self, word: str):
        return word[0] in 'aeiou' and word[-1] in 'aeiou'

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        cumulativeVowelCounts = [0]

        count = 0
        for word in words:
            if self.startsAndEndsWithVowel(word):
                count+=1
            cumulativeVowelCounts.append(count)

        result = []
        for start, end in queries:
            result.append(cumulativeVowelCounts[end + 1] - cumulativeVowelCounts[start])

        return result