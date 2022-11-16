#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        size = len(head)
        for i in range(0,size):
            if head[i] != head[size-(i+1)]:
                return(False)
        return(True)

print(Solution.isPalindrome("",[1,2,2,1]))