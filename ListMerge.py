class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"val{self.val} next{self.next}"

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:        
        def Merger(list1,list2,list3) -> ListNode:
            if list1 == None and list2 == None:
                return None
            elif list1 == None:
                return Merger(None,list2.next,ListNode(list3,list2.val))
            elif list2 == None:
                return Merger(list1.next,None,ListNode(list3.next,list1.val))
            elif list1.val < list2.val:
                return Merger(list1.next,list2,ListNode(list3.next,list1.val))
            else:
                return Merger(list1,list2.next,ListNode(list3.next,list2.val))

        return(Merger(list1,list2,ListNode()))


        
list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(4,None)))
print(list1)


#print(Solution.mergeTwoLists("",list1,list2))