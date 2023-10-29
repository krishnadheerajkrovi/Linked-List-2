'''
1. Find the length of both the linked lists. Move the longer list's head to the point where the length of both the lists is equal
2. Move both the heads until they are equal
3. Return any one of the heads

TC: O(n)
SC: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA == None or headB == None:
            return None
        
        lenA = 0
        lenB = 0
        curr = headA
        while(curr!=None):
            lenA +=1
            curr = curr.next
        curr = headB
        while(curr != None):
            lenB += 1
            curr = curr.next
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
        