# given input list of ints, output highest product from 3 ints
# obvious method, sort then multiply 3 abs(highest numbers)
# [-10, -10, 1, 3, 2] nlogn
# not O(n)
import time


def slow_highest_product(input):
    start = time.clock()
    lst = map(abs, input)
    sorted_input = sorted(lst)
    return reduce(lambda x, y: x * y, sorted_input[-3:]), time.clock() - start

def highest_product(input):
    start = time.clock()
    # keep track of prod_highest2, prod_lowest2 to account for negatives
    highest_prod3 = reduce(lambda x,y: x*y, input[:3])
    highest_prod2 = input[0]*input[1]
    highest = max(input[0], input[1])
    lowest_prod2 = input[0]*input[1]
    lowest = min(input[0], input[1])
    for current in input[2:]:
        # is there a new highest product of 3?
        highest_prod3 = max(highest_prod3, highest_prod2*current, lowest_prod2*current)
        # check highest product of 2
        highest_prod2 = max(highest_prod2, current*lowest, current*highest)
        # check lowest product of 2
        lowest_prod2 = min(lowest_prod2, current*lowest, current*highest)
        # check highest
        highest = max(current, highest)
        # check lowest
        lowest = min(current, lowest)
    return highest_prod3, time.clock()-start

print slow_highest_product([-10, -10, 1, 3, 2, 23, 24, 343,65463, -34342, 1414332, 948543])
print highest_product([-10, -10, 1, 3, 2, 23, 24, 343,65463, -34342, 1414332, 948543])