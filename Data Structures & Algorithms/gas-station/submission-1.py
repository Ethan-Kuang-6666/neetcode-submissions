class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        current = 0
        for i in range(len(gas)):

            current += gas[i]
            current -= cost[i]

            if current < 0:
                res = i + 1
                current = 0
        return res
        