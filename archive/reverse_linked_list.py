"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      curr = head
      temp = ListNode()
      prev = None
      while curr.next:
		
        temp.next = curr
        # curr.next = temp
        curr = curr.next
        prev = ListNode()
        if curr == head:
          	prev = curr
        	temp = curr.next
            curr.next = None
            curr = temp
        else:
          	temp = curr.next
            curr.next = prev
            prev = curr
        	curr = temp
      curr.next = prev            
      return curr
    
    #     .
# head = [1,2,3]




from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = ListNode()
        temp = ListNode()
        while curr:
            if curr == head:
                prev = curr
                curr = curr.next
                curr.next = None
            else:
                prev = curr
                curr = curr.next
                curr.next = prev
        curr.next = prev
        return curr         
                

#      .
#   [1,2,3]