# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_value = l1.val + l2.val  # 当前位的和
        carry = sum_value // 10  # 前一个的进位
        head = ListNode(sum_value % 10)  # 头结点
        now_node = head  # 当前结点
        next_l1, next_l2 = l1.next, l2.next
        while next_l1 is not None and next_l2 is not None:
            sum_value = next_l1.val + next_l2.val + carry
            carry = sum_value // 10
            now_node.next = ListNode(sum_value % 10)
            now_node = now_node.next
            next_l1, next_l2 = next_l1.next, next_l2.next
        if next_l1 is None:
            while next_l2 is not None:
                sum_value = next_l2.val + carry
                carry = sum_value // 10
                now_node.next = ListNode(sum_value % 10)
                now_node = now_node.next
                next_l2 = next_l2.next
        else:
            while next_l1 is not None:
                sum_value = next_l1.val + carry
                carry = sum_value // 10
                now_node.next = ListNode(sum_value % 10)
                now_node = now_node.next
                next_l1 = next_l1.next
        if carry != 0:
            now_node.next = ListNode(carry)
        return head
