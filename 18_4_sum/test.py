class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Simple but Brutal way
        import itertools
        return list(set(c for c in itertools.combinations(sorted(nums), 4) if sum(c)==target))
        # O[nlg(n) + n(n-1)(n-2)(n-3)/4!] ~ O(n^4)
