class TrieNode:
    def __init__(self):
        self.children = {}  # Maps characters to child TrieNodes
        self.word = None    # Stores complete word when this node ends a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Edge case: return empty if board or words list is empty
        if not board or not words:
            return []
        
        # BUILD TRIE SECTION
        root = TrieNode()   # Create root node of tire
        for word in words:  # Process each word in the words
            current = root  
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.word = word

        result = []
        rows, cols = len(board), len(board[0])

        def dfs(row, col, node):
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] == "#" or
                board[row][col] not in node.children):
                return
            
            char = board[row][col]
            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None
            
            board[row][col] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(row + dr, col + dc, node)
            
            board[row][col] = char
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        return result

