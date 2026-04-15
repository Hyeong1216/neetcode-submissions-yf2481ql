class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        print(count)
        print(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1 # advance time 1
            
            # no remaining tasks, fast-forward to when next task becomes available
            if not maxHeap: 
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt: # if task remains
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            
