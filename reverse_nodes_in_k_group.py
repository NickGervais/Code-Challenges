'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
    * Only constant extra memory is allowed.
    * You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:            
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        elif k <= 1:
            return head
        
        prev = None
        left = head
        right = left.next
        cur_length = 2
        while right != None:
            if cur_length % k == 0:
                next_prev = left
                next_grp = right.next
                next_node = next_grp
                while left != next_grp:
                    second = left.next
                    left.next = next_node
                    next_node = left
                    left = second
                if prev == None:
                    head = right
                else:
                    prev.next = right
                if next_grp == None:
                    break
                prev = next_prev
                left = next_grp
                right = left
                cur_length = 1
            right = right.next
            cur_length += 1
            
        return head

head = ListNode(1)
cur_node = head
for i in range(2, 6):
    cur_node.next = ListNode(i)
    cur_node = cur_node.next

result = Solution().reverseKGroup(head, 3)

while result != None:
    print(result.val)
    result = result.next

