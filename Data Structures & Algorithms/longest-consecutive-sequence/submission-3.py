class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))   # remove duplicates and sort

        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr += 1
            else:
                curr = 1

            res = max(res, curr)

        return res