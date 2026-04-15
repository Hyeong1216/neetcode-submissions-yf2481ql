class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        graph = self.buildGraph(wordList)

        return self.bfsShortestPath(graph, beginWord, endWord)

    def buildGraph(self, wordList):
        graph = {word: [] for word in wordList}
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.canTransform(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        return graph

    def canTransform(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count == 1

    def bfsShortestPath(self, graph, start, end):
        if end not in graph:
            return 0
        q = collections.deque([(start, 1)])
        visited = set([start])

        while q:
            curr_word, curr_dist = q.popleft()
            if curr_word == end:
                return curr_dist

            for nei in graph[curr_word]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, curr_dist+1))

        return 0