class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        result = []
        '''
        Step 4: Process courses in topological order

        While queue is not empty, remove a course
        Add the removed course to your result list
        For each course that depends on the current course, reduce its prerequisite count
        If any dependent course reaches zero prerequisites, add it to queue
        '''
        while q:
            course = q.popleft()
            result.append(course)

            for dependent_course in graph[course]:
                indegree[dependent_course] -= 1
                if indegree[dependent_course] == 0:
                    q.append(dependent_course)
        return result if len(result) == numCourses else[]
        '''
        Step 5: Validate the result

        Check if you processed all courses
        Return appropriate result based on whether all courses were processed
        '''
        #---------------------------------------------------------------------
        # DFS
        # if numCourses == 0:
        #     return []

        # graph = [[] for _ in range(numCourses)]
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)

        # visited = [0] * numCourses # 0 == unvisited, 1= visiting, 2= visited
        # result = []
        # def dfs(course):
        #     # when cycle detected, return empty list
        #     if visited[course] == 1:
        #         return False
            
        #     if visited[course] == 2:
        #         return True
        #     visited[course] = 1

        #     for neighbor in graph[course]:
        #         if not dfs(neighbor):
        #             return False

        #     visited[course] = 2
        #     result.append(course)
        #     return True
        # for course in range(numCourses):
        #     if visited[course] == 0:
        #         if not dfs(course):
        #             return []
        
        # return result[::-1]