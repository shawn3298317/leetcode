class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r_ptr, w_ptr = 0, 0
        
        while r_ptr != len(nums):
            
            if nums[r_ptr] == val:
                r_ptr += 1
                continue
            else:
                nums[w_ptr] = nums[r_ptr]
                w_ptr += 1
                r_ptr += 1
        
        while w_ptr != r_ptr:
            nums.pop(-1)
            w_ptr += 1
        
        return len(nums)
