#
# James A. Chase
# 061024
#
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node

    def __eq__(self, other: 'ListNode') -> bool:
        return self.val == other.val

    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'

    def __repr__(self) -> str:
        return self.__str__()


def form_linked_list(arr: List[int]) -> ListNode:
    assert len(arr) > 0

    idx = 0
    n = len(arr) - 1
    head = ListNode(arr[idx])
    ptr = head
    while idx < n:
        idx += 1
        node = ListNode(arr[idx])
        ptr.next = node
        ptr = ptr.next
    return head


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        carry = 0

        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            total = d1 + d2 + carry
            carry, val = divmod(total, 10)

            ptr.next = ListNode(val)
            ptr = ptr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
