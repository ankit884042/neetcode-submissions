class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # still sort, for dedup ordering
        res = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.add(tuple(sorted((nums[i], nums[j], complement))))
                seen.add(nums[j])
        return [list(t) for t in res]