def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left_half = mergeKLists(lists[:mid])
    right_half = mergeKLists(lists[mid:])

    return mergeTwoLists(left_half, right_half)


def mergeTwoLists(l1, l2):
    dummy_node = ListNode(0)
    current = dummy_node

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy_node.next