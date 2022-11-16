class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        def Sort(Sorted,list1,list2):
            if list1.val == None and list2.val == None:
                return Sorted
            elif list1.val != None:
                Sorted.append(list1.val)
                return Sort(Sorted,list1.next,list2)
            elif list2.val != None:
                Sorted.append(list2.val)
                return Sort(Sorted,list1,list2.next)
            else:
                if list1.val < list2.val:
                    Sorted.append(list1.val)
                    return Sort(Sorted,list1.next,list2)
                else:
                    Sorted.append(list2.val)
                    return Sort(Sorted,list1,list2.next)
        return(Sort([],list1,list2))
list1,list2 = ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}} ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
print(Solution.mergeTwoLists("",list1,list2))
