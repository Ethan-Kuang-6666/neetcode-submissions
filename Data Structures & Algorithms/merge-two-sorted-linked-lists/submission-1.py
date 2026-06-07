# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        current = start
        one = list1
        two = list2

        while one or two:
            temp = None
            if one and two:
                if one.val <= two.val:
                    temp = one
                    one = one.next
                else:
                    temp = two
                    two = two.next

                current.next = temp
                current = current.next

            else:
                temp = one if one else two
                current.next = temp
                break

        return start.next
        



        