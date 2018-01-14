class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #list to map: (num, count)
        from collections import Counter
        nums_map = Counter(nums) #O(n)
            
        answer = []
        
	#O(n)
        for n in nums:
            if target-n in nums_map:
                if n == target-n:
                    if nums_map[n] > 1:
                        ans = []
                        for i, nn in enumerate(nums):
                            if nn == n and i not in ans:
                                ans.append(i)
                            if len(ans) == 2:
                                return ans
                else:
                    return [nums.index(n), nums.index(target-n)]
        
        return answer
