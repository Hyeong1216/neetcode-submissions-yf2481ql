class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Questions
        # 1. What happens when there is no endword in wordList, otherwise there's no way

        if endWord not in wordList:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    print(next_word)
                    if next_word in wordList and next_word not in visited:
                        queue.append((next_word, steps + 1))
                        visited.add(next_word)
        return 0
