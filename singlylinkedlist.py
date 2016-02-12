# delete a node from singly-linked list given only variable pointing to the node
# ie. delete_node(b)
# walk through list to the node, then fix pointers to next
# if node.next = b, node.next = node.next.next
# oh nvm only have information about reference to node we want to delete


def delete_node(node_to_delete):
    # get the next node from input
    next_node = node_to_delete.next

    if next_node:
        # modify the input node's value & pointer
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        raise Exception("can't delete the last node")


# this might have dangling nodes
# check for cycles


def contains_cycle(first_node):
    #  check 2 ahead and then compare
    current = first_node
    ahead = first_node

    while ahead is not None and ahead.next is not None:
        current = current.next
        ahead = ahead.next.next

        if ahead == current:
            return True

    return False


def reverse(first_node):
    # reverse in place linked list
    # going through from tail to end isn't effective, want O(n) sol'n
    # change next pointer of each node to previous
    current_node = first_node
    previous_node = None
    next_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        # step forward
        previous_node = current_node
        current_node = next_node

    return previous_node


def kth_node(first_node, k):
    # find the kth to last node
    ahead_node = first_node
    current_node = first_node
    # make ahead_node k - 1 ahead
    for i in xrange(k-1):
        if not ahead_node.next:
            raise LookupError("K is longest than list")
        ahead_node = ahead_node.next
    # step the nodes forward until right node hits the end of the list
    while ahead_node:
        current_node.next
        ahead_node.next
    return current_node
