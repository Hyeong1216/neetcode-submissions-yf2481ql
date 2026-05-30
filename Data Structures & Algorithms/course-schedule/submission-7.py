class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Questions
        # 1. Can there be duplicate prerequisites?
        # 2. Can numCourses be 0?

        # approaches
# BFS vs DFS 핵심 차이
# DFS (Depth First Search)
# 그래프:
# 0 → 1 → 3
# ↓
# 2

# 탐색 순서: 0 → 1 → 3 → 2

# 한 방향으로 끝까지 파고들어
# Stack (또는 재귀) 사용
# Cycle detection에 자연스러워 — 지금 가고 있는 경로에 이미 방문한 노드 나오면 cycle

# BFS (Breadth First Search)
# 그래프:
# 0 → 1 → 3
# ↓
# 2

# 탐색 순서: 0 → 1 → 2 → 3

# 레벨 단위로 퍼져나가
# Queue 사용
# 최단거리에 자연스러워 (#127 Word Ladder가 이거였어)

        # DFS
        # Build adjacency list - what prerequisites does each course have?
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        state = [0] * numCourses # 0=unvisited, 1=visiting, 2=visited

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2

            return True






        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

































