class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #this could definitely be faster
        def isValidTransform(currWord, word):
            diff = False
            for i in range(len(currWord)):
                if currWord[i] != word[i]:
                    if diff:
                        return False
                    diff = True
            return True

        if endWord not in wordList:
            return 0
        
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        result = 1

        while q:
            for _ in range(len(q)):
                currWord = q.popleft()

                if currWord == endWord:
                    return result

                for word in wordList:
                    if word not in visited and isValidTransform(currWord, word):
                        q.append(word)
                        visited.add(word)
            
            result += 1
                

        return 0