# Balance index
# Write a method called Balance Index that will efficiently find the index in an array of integers where the sum of the values on each side of the index are equal. Return -1 if no such index exists.  Do not include the value at the index in the left or right sum. At index 0 the left sum should evaluate to zero; at the last index the right sum should evaluate to zero. 

# Examples
# [2, 1, 4, 3] should return an index of 2
# [-1, 3, 2, -3] should return an index of 1
# [5, -1, 1] should return an index of 0
# [1, 2, 3] should return -1
# [5] should return 0

def balanceIndex(array):
    #have two counts, left and right
    #go in each direction, store sum from each
    for x in range(len(array)):
        rightsum=sum(array[x+1:])
        leftsum=sum(array[:x])
        if leftsum == rightsum:
            return x
    return -1

print balanceIndex([2, 1, 4, 3])
print balanceIndex([-1, 3, 2, -3])