# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        GroupPrev=dummy
        while True:
             Kth=self.Get_Kth(GroupPrev,k)
             if not Kth:
                break
             GroupNext=Kth.next
             prev=Kth.next
             current=GroupPrev.next
             while current != GroupNext:
                  tmp=current.next
                  current.next=prev
                  prev=current
                  current=tmp
             tmp=GroupPrev.next
             GroupPrev.next=Kth
             GroupPrev=tmp
        return dummy.next    


    def Get_Kth(self,current,k):
            while current and k>0:
                  current=current.next
                  k-=1  
            return current       
