# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       dummy = ListNode()
       curr = dummy

       while list1 and list2:
        
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
            
        else:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
            
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(6)
    node4 = ListNode(3)
    node5 = ListNode(5)
    node6 = ListNode(7)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6

    merger = Solution()
    print(merger.mergeTwoLists(node1, node4))
