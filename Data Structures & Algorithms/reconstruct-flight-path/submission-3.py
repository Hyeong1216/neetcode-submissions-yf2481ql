class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)
        result = []
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                result.append(stack.pop())


        return result[::-1]
        #-------------------------------------------
        # DFS
        # graph = defaultdict(list)
        # for i, (src, dst) in enumerate(tickets):
        #     graph[src].append((dst, i))
        
        # for src in graph:
        #     graph[src].sort()

        # used = [False] * len(tickets)

        # def dfs(airport, path, remaining_tickets):
        #     if remaining_tickets == 0:
        #         return path[:]

        #     for (dst, i) in graph[airport]:
        #         if not used[i]:
        #             used[i] = True
        #             path.append(dst)

        #             result = dfs(dst, path, remaining_tickets-1)
        #             if result:
        #                 return result
                    
        #             path.pop()
        #             used[i] = False
        #     return None
            
        # return dfs("JFK", ["JFK"], len(tickets))

        #DFS
        # graph = defaultdict(list)
        # for i, (src, dst) in enumerate(tickets):
        #     graph[src].append((dst, i))

        # for src in graph:
        #     graph[src].sort()

        # used = [False] * len(tickets)

        # def dfs(airport, path, remaining_tickets):
        #     if remaining_tickets == 0:
        #         return path[:]
            
        #     for dst, ticket_idx in graph[airport]:
        #         if not used[ticket_idx]:
        #             used[ticket_idx] = True
        #             path.append(dst)

        #             result = dfs(dst, path, remaining_tickets-1)
        #             if result:
        #                 return result

        #             path.pop()
        #             used[ticket_idx] = False
        #     return None


        # return dfs("JFK", ["JFK"], len(tickets))