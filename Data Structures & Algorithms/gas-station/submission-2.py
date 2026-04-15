class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0

        for i in range(len(gas)):
            # TODO: Update tank with net gain/loss at station i
            tank = tank + gas[i] - cost[i]
            # TODO: If tank becomes negative, what should we do?
            if tank < 0:
                start = i+1
                tank = 0

        
        return start
        #---------------------------------------------------------
        # brute force
        # n = len(gas)

        # for start in range(n):
        #     tank = 0
        #     stations_visited = 0
        #     current = start

        #     while stations_visited < n:
        #         tank += gas[current]
        #         if tank >= cost[current]:
        #             tank -= cost[current]
        #             current = current + 1 if (current + 1 ) < n else 0
        #             stations_visited +=1

        #         else:
        #             break                    


        #     if stations_visited == n:
        #         return start

        # return -1
