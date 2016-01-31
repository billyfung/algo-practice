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

