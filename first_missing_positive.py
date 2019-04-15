"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = None
        for i in nums:
            if max_val == None:
                max_val = i
            elif max_val < i:
                max_val = i

        if max_val == None or max_val < 1:
            return 1
        
        new_nums = [None] * (max_val + 2)
        
        for num in nums:
            if num > 0:
                new_nums[num] = num
        
        for i in range(1, len(new_nums)):
            if new_nums[i] == None:
                return i

input = [7,8,9,11,12]
result = Solution().firstMissingPositive(input)
print(result)