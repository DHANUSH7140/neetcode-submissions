from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return len(c) != len(nums)