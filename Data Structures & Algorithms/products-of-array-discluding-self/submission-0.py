class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        rev = nums[::-1]
        pre_muls = []
        post_muls = []
        muls = []
        n = len(nums)
        for i in nums:
            val = val*i
            pre_muls.append(val)
        val = 1
        for i in rev:
            val = val*i
            post_muls.append(val)
        post_muls = post_muls[::-1]
        muls.append(post_muls[1])
        for i in range(1,n-1):
            muls.append(pre_muls[i-1]*post_muls[i+1])
        muls.append(pre_muls[n-2])
        return muls
