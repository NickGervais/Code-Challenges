"""
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS:
--------------------------------------------------------------

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        longest = 0
        left = 0
        right = 1

        seen_indx = {s[left]: left}
        while right < len(s):
            cur_char = s[right]
            if seen_indx.get(cur_char) != None:
                i = seen_indx[cur_char]
                if i >= left and i < right:
                    cur_length = right - left
                    if longest < cur_length:
                        longest = cur_length
                    left = i + 1
                seen_indx[cur_char] = right
                right += 1
            else:
                seen_indx[cur_char] = right
                right += 1

        if longest < right - left:
            longest = right - left

        return longest


input_1 = "abcabcbb"
input_2 = "bbbbb"
input_3 = "pwwkew"

sol_class = Solution()
result_1 = sol_class.lengthOfLongestSubstring(input_1)
result_2 = sol_class.lengthOfLongestSubstring(input_2)
result_3 = sol_class.lengthOfLongestSubstring(input_3)

print "Input 1:", input_1, "Result 1:", result_1
print "Input 2:", input_2, "Result 2:", result_2
print "Input 3:", input_3, "Result 3:", result_3
