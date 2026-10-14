class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        rev = nums[::-1]
        pre_muls = []
        post_muls = []
        muls = []
        n = len(nums)
        for i in nums[:-1]:
            val = val*i
            pre_muls.append(val)
        val = 1
        for i in rev[:-1]:
            val = val*i
            post_muls.append(val)
        post_muls = post_muls[::-1]
        muls.append(post_muls[0])
        for i in range(n-2):
            muls.append(pre_muls[i]*post_muls[i+1])
        muls.append(pre_muls[-1])
        return muls
