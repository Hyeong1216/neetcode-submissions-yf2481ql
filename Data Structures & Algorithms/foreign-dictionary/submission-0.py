class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: [] for word in words for char in word}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    break
        
        state = {char: 0 for char in graph}
        result = []

        def dfs(char):
            if state[char] == 1:
                return False
            
            if state[char] == 2:
                return True
            
            state[char] = 1

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            
            state[char] = 2
            result.append(char)
            return True
        
        for char in graph:
            if not dfs(char):
                return ""
        return ''.join(reversed(result))

