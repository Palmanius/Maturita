class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __repr__(self) -> str:
    #     return f"Nodes(val = {self.val} and next = {self.next})."

new = ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))

def Mapper(list:ListNode):
    if list.next != None:
        print(list.val)
        return Mapper(list.next)
    else:
        return(list.val)
print(Mapper(new))