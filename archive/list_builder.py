from typing import Optional, List
import random
import sys
class TreeNode:
    def __init__(self, value: int = 0, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, value: int = 0, next = None) -> None:
        self.value = value
        self.next = next

class Helper:

    def __init__(self) -> None:
        pass

    def insertTreeNode(node: TreeNode) -> None:
        pass

    def createLinkedList(self, li: Optional[List[int]] = None):    
        if li is not None:
            # Take a list of integers and turn it into a linked list. Sorted.
            pass
        else:
            no_of_nodes = int(input("How many nodes would you like? "))
            values = []
            for i in range(no_of_nodes):
                values.append(random.randrange(1, 1200))
            root = self.insertLinkNode(value=values[0])
            for i in range(1, len(values)):
                self.insertLinkNode(root,values[i])
        return root

    def insertLinkNode(self, root: ListNode = None, value: int = 0) -> None:
        new_node = ListNode(value=value)
        curr = root
        if not root:
            root = new_node
            return root
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return root

if __name__ == "__main__":
    my_helper = Helper() 
    if sys.argv[1] == "1":
        my_linked_list = my_helper.insertLinkNode(value=7)
        print(str(my_linked_list))
    if sys.argv[1] == "2":
        baba = my_helper.createLinkedList()
        print("linked list cast to str: ", str(baba))
        toosh = []
        while baba:
            toosh.append(baba.value)
            baba = baba.next
        print(toosh)           

    def createTree():
        pass

    def createLinkedList():
        pass 
        
