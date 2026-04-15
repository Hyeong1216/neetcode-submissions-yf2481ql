class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)] # 1 indexed

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(len(edges)-1, -1, -1):
            a, b = edges[i]
            if self.is_connected(graph, n, a, b):
                return [a, b]

    def is_connected(self, graph, n, ignore_a, ignore_b):
        visited = set()
        q = collections.deque([1])
        visited.add(1)
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if (node == ignore_a and neighbor == ignore_b) or \
                (node == ignore_b and neighbor == ignore_a):
                    continue
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return n == len(visited)