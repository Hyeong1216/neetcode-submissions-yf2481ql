class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force
        n = len(gas)

        for start in range(n):
            tank = 0
            stations_visited = 0
            current = start

            while stations_visited < n:
                tank += gas[current]
                if tank >= cost[current]:
                    tank -= cost[current]
                    current = current + 1 if (current + 1 ) < n else 0
                    stations_visited +=1

                else:
                    break                    


            if stations_visited == n:
                return start

        return -1
