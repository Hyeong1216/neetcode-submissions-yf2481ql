# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.word = None
                
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        # Build trie from word list
        root = TrieNode()
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.word = word
        
        result = []
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, node):
            # Boundary checks and character match
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
                board[row][col] == '#' or board[row][col] not in node.children):
                return
            
            # Get current character and move to next trie node
            char = board[row][col]
            node = node.children[char]
            
            # Check if we found a complete word
            if node.word:
                result.append(node.word)
                node.word = None  # Avoid duplicates
            
            # Mark cell as visited
            board[row][col] = '#'
            
            # Explore all 4 directions
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(row + dr, col + dc, node)
            
            # Backtrack: restore original character
            board[row][col] = char
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return result