# given 2 sorted lists merge them 1 create 1 sorted merged list
# lazy way is built in sort, O(nlogn)
# faster way is O(n)


def merge_lists(list_A, list_B):
    merged_size = len(list_A) + len(list_B)
    merged_list = [None] * merged_size
    current_A_index, current_B_index, current_merged_index = 0
    while current_merged_index < merged_size:
        # check if at end of either list
        is_A_empty = current_A_index >= len(list_A)
        is_B_empty = current_B_index >= len(list_B)
        # if next item comes from list A
        if not is_A_empty and (is_B_empty or list_A[current_A_index]<list_B(current_B_index)):
            merged_list[current_merged_index] = list_A[current_A_index]
            current_A_index += 1
        else:
            # next item comes from list B
            merged_list[current_merged_index] = list_B[current_B_index]
            current_B_index += 1
        current_merged_index += 1
    return merged_list

