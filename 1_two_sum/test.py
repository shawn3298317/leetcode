class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
	
	O(nlg(n) + n) ~ O(nlg(n))
	Need to sort nums first,
	then maintain two pointers to trace value.
        """
        nums = sorted(nums)
        
        i, j = 0, len(nums)-1
        answer_set = []
        while i < j:
            two_sum = nums[i] + nums[j]
            
            if two_sum == target:
                answer_set = [i, j]
                break
            elif two_sum < target:
                i+=1
            else:
                j-=1
                
        return answer_set
