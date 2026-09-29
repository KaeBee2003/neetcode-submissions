class Solution:
    def sortArray(self, nums):
        n = len(nums)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # Extract elements from the heap
        for i in range(n - 1, 0, -1):
            # Move largest element to the end
            nums[0], nums[i] = nums[i], nums[0]

            # Restore heap
            self.heapify(nums, i, 0)

        return nums

    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check left child
        if left < n and nums[left] > nums[largest]:
            largest = left

        # Check right child
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If parent isn't largest, swap and continue
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]

            self.heapify(nums, n, largest)