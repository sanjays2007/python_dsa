class Solution:
    def prefixAvg(self, arr):
        running_sum = 0
        result = []

        for i, num in enumerate(arr):
            running_sum += num
            # Use floor division '//' to automatically get the floor of the average
            result.append(running_sum // (i + 1))

        return result
