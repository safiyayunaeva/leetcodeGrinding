# testing username

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    """
        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.

        It can be solved with 2 pointers when right is shifted by nth elements
    """
    dummy = Node(0, head)
    left = dummy
    right = dummy
    # right is shifted by n
    while n > 0 and right:
        right = right.next
        n = n - 1

    # next step shift both pointers till

    while right:
        left = left.next
        right = right.next

    # when right reaches Null - left is on the node prev to the node we need to delete
    # delete next node
    left.next = left.next.next

    return dummy.next
