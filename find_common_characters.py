"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        word = A.pop(0)
        for char in word:
            num_found = 0
            for s in range(len(A)):
                cur_s = A[s]
                in_cur_s = False
                i = 0
                while not in_cur_s and i < len(cur_s):
                    if cur_s[i] == char:
                        in_cur_s = True
                        num_found += 1
                        cur_s = cur_s[:i] + cur_s[i+1:]
                    i += 1
                A[s] = cur_s
            if num_found == len(A):
                result.append(char)
        return result 

given = ["bella","label","roller"]
result = Solution().commonChars(given)
print(result)
