class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a = []
        n = len(nums)
        nums.sort()
        for j in range(0,n-2):
            i = j+1
            k = n-1
            target = -nums[j]
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            elif nums[j] > 0:
                break
            elif nums[j] + nums[n-2] + nums[n-1] < 0:
                continue
            else:
                pass
            
            while i < k:
                s = nums[i] + nums[k]
                if s > target:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

                elif s < target:
                    i += 1
                    while i < k and nums[i] == nums[i-1]:
                        i += 1

                else:
                    a.append([nums[i],nums[j],nums[k]])
                    i += 1
                    while i < k and nums[i] == nums[i-1]:
                        i += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return a 