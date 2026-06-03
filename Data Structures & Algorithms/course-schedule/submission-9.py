class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1: return False
            if state[course] == 2: return True
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
        # Questions:
        # 1. Can there be duplicate prerequisites?
        # 2. Can numCourses be 0?

        # Approach 1: DFS cycle detection — O(V + E)
        # state: 0=unvisited, 1=visiting, 2=visited
        # if we hit a node with state=1 → cycle detected
        
        # graph = [[] for _ in range(numCourses)]
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)
        # state = [0] * numCourses

        # def dfs(course):
        #     if state[course] == 1: return False  # cycle
        #     if state[course] == 2: return True   # already processed
        #     state[course] = 1
        #     for next_course in graph[course]:
        #         if not dfs(next_course):
        #             return False
        #     state[course] = 2
        #     return True

        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False
        # return True

        # Approach 2: BFS Topological Sort — O(V + E)
        # Key insight: if cycle exists, some nodes never reach indegree=0
        # processed_count == numCourses → no cycle → can finish

        # 1. Build adjacency list
        # graph = [[] for _ in range(numCourses)]
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)

        # # 2. Calculate in-degree (# of prereqs per course)
        # indegree = [0] * numCourses
        # for course, prereq in prerequisites:
        #     indegree[course] += 1

        # # 3. Start BFS from courses with no prerequisites
        # q = deque()
        # for course in range(numCourses):
        #     if indegree[course] == 0:
        #         q.append(course)

        # # 4. Process courses, reducing indegree of dependents
        # processed_count = 0
        # while q:
        #     course = q.popleft()
        #     processed_count += 1
        #     for next_course in graph[course]:
        #         indegree[next_course] -= 1
        #         if indegree[next_course] == 0:
        #             q.append(next_course)

        # return processed_count == numCourses

        # Time: O(V + E) — V courses, E prerequisites
        # Space: O(V + E) — graph + indegree array