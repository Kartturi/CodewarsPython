# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(l1.next.next.next)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = l1
        q = l2
        current = dummy
        carry = 0

        while (p is not None or q is not None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum / 10
            current.next = ListNode(sum % 10)
            current = current.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next


print(Solution.addTwoNumbers(l1, l2))
