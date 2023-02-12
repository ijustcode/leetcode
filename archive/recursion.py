# This function reverses a string. Using recursion.
import sys

class ListNode:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next
class TreeNode:
    def __init__(self, value, left, right) -> None:
        self.value = value
        self.right = right
        self.left = left

class Solution:

    def __init__(self, height: int = 2) -> None:
        self.height = height

    def reverseString(self, word: str) -> str:
        if word == '':
            return ''
        return self.reverseString(word[1:]) + word[0]
    
    def decToBinary(self, dec: int, all_outs: str) -> str:
        if dec == 0:
            return all_outs
        all_outs = str(dec % 2) + all_outs
        return self.decToBinary(int(dec / 2), all_outs)

    def reverseLinkedList(self, root: ListNode) -> ListNode:
        if not root:
            return None 
        else: 
            previous = root
            root = root.next
            root.next = previous
            return self.reverseLinkedList(root.next)
    
    def mergeSortedLinkedLists(self, root_a: ListNode, root_b: ListNode) -> ListNode:
        if not root_a:
            return root_b
        if not root_b:
            return root_a
        if root_a.value < root_b.value:
            root_a.next = self.mergeSortedLinkedLists(root_a.next, root_b)
            return root_a
        elif root_a.value > root_b.value:
            root_a.next = self.mergeSortedLinkedLists(root_a, root_b.next)
            return root_b

    def insertNodeInBST(self, root: TreeNode, insertion: TreeNode) -> TreeNode:
        if not root:
            return insertion
        else:
            if insertion.value < root.value:
                return self.insertNodeInBST(root.left, insertion)
            else:
                return self.insertNodeInBST(root.right, insertion)
    
    def printLeafNodesBST(self, root: TreeNode) -> list(TreeNode):
        results = []
        if not root:
            return None
        curr = root.next
        self.printLeafNodesBST(curr)
        if root.left is None and root.right is None:
            results.append(root)
        

if __name__ == "__main__":

    com_line_args = sys.argv
    my_solution = Solution(17)
    if com_line_args[1] == '1':            
        word = input("Enter your word: ")
        my_var = my_solution.reverseString(word)
        print(my_var)
        print(type(my_solution.height))
        print(my_solution.height)
    if com_line_args[1] == '2':
        print("all of arguments: ", str(sys.argv[1]))
    if com_line_args[1] == '3':
        print(my_solution.decToBinary(233, ""))