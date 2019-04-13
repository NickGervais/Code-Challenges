"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        if len(trust) == 0:
            return 1
        
        times_trusted = {}
        trusts_others = set()
        
        for i in range(len(trust)):
            a, b = trust[i]
            trusts_others.add(a)
            if times_trusted.get(b):
                times_trusted[b] += 1
            else:
                times_trusted[b] = 1
            
        judge_found = False
        judge_label = None
        for person, count in times_trusted.items():
            if count == N - 1 and not person in trusts_others:
                if not judge_found:
                    judge_found = True
                    judge_label = person
                else:
                    return -1
        
        if judge_found:
            return judge_label
        
        return -1

N = 4         
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
result = Solution().findJudge(N, trust) 
print(result)       