class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let A[i] represent the minimum cost to reach step i
        # General Case: A[i] = min(A[i - 1], A[i - 2]) + cost[i]
        # Base Case: A[0] = cost[0], A[1] = cost[1]
        two_behind = cost[0]
        behind = cost[1]

        for i in range(2, len(cost)):
            curr = min(behind, two_behind) + cost[i]
            two_behind = behind
            behind = curr
        
        return min(behind, two_behind)
        