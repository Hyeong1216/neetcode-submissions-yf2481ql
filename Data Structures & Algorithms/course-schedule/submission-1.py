class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list - what prerequisites does each course have?
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        state = [0] * numCourses # 0 = unvisited, 1 = visiting, 2 = visited

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