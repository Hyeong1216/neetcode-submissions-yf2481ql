class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS
        if numCourses == 0:
            return []

        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses # 0 == unvisited, 1= visiting, 2= visited
        result = []
        def dfs(course):
            # when cycle detected, return empty list
            if visited[course] == 1:
                return False
            
            if visited[course] == 2:
                return True
            visited[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2
            result.append(course)
            return True
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return []
        
        return result[::-1]