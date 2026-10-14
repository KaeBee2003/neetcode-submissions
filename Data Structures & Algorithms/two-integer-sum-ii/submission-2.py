class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        two_sum = numbers[i] + numbers[j]
        while j > i:
            if two_sum == target:
                return [i+1,j+1]
            # code to move i and j
            elif two_sum > target:
                j -= 1
            else:
                i += 1
            two_sum = numbers[j] + numbers[i]