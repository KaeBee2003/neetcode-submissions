class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            mid = end - start // 2 + start
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return start