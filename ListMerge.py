class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"Nodes(val = {self.val} and next = {self.next})."
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        def Merger(SortedList:ListNode,list1:ListNode,list2:ListNode) -> ListNode:
            if list1.next == None or list2.next == None:
                if list1.next != None:
                    return Merger(ListNode(list1.val,SortedList),list1.next,list2)
                elif list2.next != None:
                    return Merger(ListNode(list2.val,SortedList),list1,list2.next)
                else: 
                    if list1.val > list2.val:
                        return(ListNode(list2.val,list1.val))
                    else:
                        return(ListNode(list1.val,list2.val))
            else:
                if list1.val > list2.val:
                    return Merger(ListNode(list1.val,SortedList),list1.next,list2)
                else: 
                    return Merger(ListNode(list2.val,SortedList),list1,list2.next)
        return(Merger(ListNode(),list1,list2))




list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(4,None)))
print(Solution.mergeTwoLists([],list1,list2))
