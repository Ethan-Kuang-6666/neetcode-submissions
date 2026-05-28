class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            current = [max(t[0], current[0]), max(t[1], current[1]), max(t[2], current[2])]
            if current == target:
                return True

        return False