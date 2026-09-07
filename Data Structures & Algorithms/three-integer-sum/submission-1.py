class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = sorted(nums)
        n = len(result)
        lst = []

        for i in range(n):
            if i > 0 and result[i] == result[i - 1]:
                continue
            if result[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                total = result[i] + result[l] + result[r]
                if total == 0:
                    lst.append([result[i], result[l], result[r]])
                    l += 1
                    r -= 1
                    while l < r and result[l] == result[l - 1]:
                        l += 1
                    while l < r and result[r] == result[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return lst