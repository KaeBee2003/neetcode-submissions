import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        while max_k > min_k:
            mid_k = (min_k + max_k) // 2
            hours = sum(math.ceil(pile / mid_k) for pile in piles)
            if hours > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k
        return min_k