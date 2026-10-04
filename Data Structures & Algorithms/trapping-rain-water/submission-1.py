class Solution:
    def trap(self, height: List[int]) -> int:
        r_max = []
        curr_max = 0
        n = len(height)
        for i in range(n):
            curr_val = height[i]
            if curr_val > curr_max:
                curr_max = curr_val
            r_max.append(curr_max)
        l_max = []
        curr_max = 0
        for i in range(n-1,-1,-1):
            curr_val = height[i]
            if curr_val > curr_max:
                curr_max = curr_val
            l_max.append(curr_max)
        ll_max = l_max[::-1]
        val = 0
        for i in range(n):
            val += min(ll_max[i],r_max[i]) - height[i]
        return val
                        