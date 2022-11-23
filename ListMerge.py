class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"val {self.val} next {self.next}"

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        def Merger(self,list1:ListNode,list2:ListNode) -> ListNode:
            if list1 == None and list2 == None:
                return self
            elif list1 == None:
                return Merger(ListNode(self,list2.val),None,list2.next)
            elif list2 == None:
                return Merger(ListNode(self,list1.val),list1.next,None)
            else:
                if list1.val > list2.val:
                    return Merger(ListNode(self,list2.val),list1,list2.next)
                else:
                    return Merger(ListNode(self,list1.val),list1.next,list2)
        
        return Merger(ListNode(),list1,list2)

list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(4,None)))
print(Solution.mergeTwoLists(ListNode(),list1,list2))
