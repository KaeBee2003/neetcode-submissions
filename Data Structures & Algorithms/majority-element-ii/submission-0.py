class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)
        for number in nums:
            counter[number] += 1

        a = []
        for k,v in counter.items():
            if v > len(nums)//3:
                a.append(k)
        return a 
            