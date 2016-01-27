# input list and index
# output, product of all numbers except @ index
# input = [1,2,6,5,9]
# [540, 270, 90, 108, 60]
# [2*6*5*9, 1*6*5*9, 1*2*6*9, 1*2*6*5]


def product_other_numbers(lst):
    # we can see that product = product of numbers before index * product numbers after index
    # product before each index
    product_all = [None] * len(lst)
    product_so_far = 1
    for i in range(len(lst)):
        product_all[i] = product_so_far
        product_so_far *= lst[i]
    # product of numbers after the index * before index
    product_so_far = 1
    for i in range(len(lst)-1,-1,-1):
        product_all[i] *= product_so_far
        product_so_far *= lst[i]

    return product_all

print product_other_numbers([1,7,3,4])