class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"Nodes(val = {self.val} and next = {self.next})."
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        def Merger(SortedList:ListNode,list1:ListNode,list2:ListNode) -> ListNode:
            




list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(4,None)))
print(Solution.mergeTwoLists([],list1,list2))
