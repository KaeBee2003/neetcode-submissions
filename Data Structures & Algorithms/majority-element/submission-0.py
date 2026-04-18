class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list({x for x in nums})
        for i in range(len(unique)):
            if nums.count(unique[i]) > (len(nums)/2):
                return unique[i]