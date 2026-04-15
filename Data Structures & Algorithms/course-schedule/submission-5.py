class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort (Khan's Algorithm, BFS-based)
        # 1. adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 2. calculate in-degree
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            indegree[course] += 1
        
        q = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        processed_count = 0
        while q:
            course = q.popleft()
            processed_count += 1

            for dependent_course in graph[course]:
                indegree[dependent_course] -= 1

                if indegree[dependent_course] == 0:
                    q.append(dependent_course)
        return processed_count == numCourses

        #-----------------------------------------------------------------------
        # DFS
        # 1. create adjacency list -> populate it with graph[course].append(prereq)
        # 2. create state list with 0 with length of numCourses
        # 3. 0 = unvisited, 1 = visiting, 2 = visited
        # 4. dfs method(course)
        # graph = [[] for _ in range(numCourses)]
        # for course, prereq in prerequisites:
        #     graph[course].append(prereq)
        
        # state = [0] * numCourses

        # def dfs(course):
        #     if state[course] == 1:
        #         return False
        #     if state[course] == 2:
        #         return True
            
        #     state[course] = 1

        #     for prereq in graph[course]:
        #         if not dfs(prereq):
        #             return False
        #     state[course] = 2

        #     return True
        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False
        # return True













        #------------------------------------------------------------------
        # DFS solution
        # Build adjacency list - what prerequisites does each course have?
        # graph = [[] for _ in range(numCourses)]
        
        # for course, prereq in prerequisites:
        #     graph[course].append(prereq)
        
        # state = [0] * numCourses # 0 = unvisited, 1 = visiting, 2 = visited

        # def dfs(course):
        #     if state[course] == 1:
        #         return False
            
        #     if state[course] == 2:
        #         return True
            
        #     state[course] = 1

        #     for prereq in graph[course]:
        #         if not dfs(prereq):
        #             return False

        #     state[course] = 2

        #     return True
        
        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False

        # return True
        #-----------------------------------------------------------------
        # BFS solution

        