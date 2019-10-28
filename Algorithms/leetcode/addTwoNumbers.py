# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arone, artwo = getinlist(l1), getinlist(l2)
        one = int(''.join(map(str, reversed(arone))))
        two = int(''.join(map(str, reversed(artwo))))
        addedstr = str(one+two)
        added = list(reversed(addedstr))
        print(added)
        totlen = len(added)
        
        head = ListNode(added.pop(0))
        point = head
        while True:
            if len(added) == 0:
                break
            tmp = ListNode(added.pop(0))
            point.next = tmp
            point = point.next
            #print(point)
        
        return head

def getinlist(topNode: ListNode):
    arr = []
    onetmp = topNode
    while True:
        if onetmp is None:
            break
        arr.append(onetmp.val)
        onetmp = onetmp.next
    return arr