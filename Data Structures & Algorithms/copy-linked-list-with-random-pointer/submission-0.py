"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = Node(0)
        tail = start
        dict = {}

        current = head

        while current:
            newNode = Node(current.val)
            tail.next = newNode
            tail = tail.next
            dict[current] = newNode
            current = current.next

        current = head
        tail = start.next
        while current:
            if current.random:
                tail.random = dict[current.random]

            tail = tail.next
            current = current.next

        return start.next



        
