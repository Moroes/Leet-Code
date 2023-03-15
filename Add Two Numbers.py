"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

""" 753865680 + 798580876  = 1552446556"""
"""
l1 =
[0,8,6,5,6,8,3,5,7]
l2 =
[6,7,8,0,8,5,8,9,7]
1285 / 1568 testcases passed
Output
[4,4,4,7,6,9,3,7,8]
Expected
[6,5,5,6,4,4,2,5,5,1]
"""

from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        end = ListNode(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_sum(lst: Optional[ListNode]):
            summ = str(lst.val)
            while lst.next:
                lst = lst.next
                summ += str(lst.val)
            return summ

        def reverse_str(number:str):
            return int(number[::-1])

        res = reverse_str(get_sum(l1)) + reverse_str(get_sum(l2))
        answ = ListNode(res % 10)
        res //= 10
        while res != 0:
            answ.append(res % 10)
            res //= 10

        return answ
