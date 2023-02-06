class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
    
node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(7)

node1.next = node2
node2.next = node3
        

current = node1

while current.next != None:
    temp = current.val
    print(temp)
    current = current.next