class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #DFS
        graph = defaultdict(list)
        for i, (src, dst) in enumerate(tickets):
            graph[src].append((dst, i))

        for src in graph:
            graph[src].sort()

        used = [False] * len(tickets)

        def dfs(airport, path, remaining_tickets):
            if remaining_tickets == 0:
                return path[:]
            
            for dst, ticket_idx in graph[airport]:
                if not used[ticket_idx]:
                    used[ticket_idx] = True
                    path.append(dst)

                    result = dfs(dst, path, remaining_tickets-1)
                    if result:
                        return result
                    path.pop()
                    used[ticket_idx] = False
            return None


        return dfs("JFK", ["JFK"], len(tickets))