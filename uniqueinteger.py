# given list of integers, containing duplicates and 1 unique
# find the 1 unique integer
# XOR


def find_unique(id_list):
    unique = 0
    for num in id_list:
        unique ^= num
    return unique

print(find_unique([123,123,23,23,5]))