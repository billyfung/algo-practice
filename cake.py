# tuple describing the cake weight (weight_in_kg, value_in_pounds)
# limited number of cakes, but unlimited supply of specific cake
# have bag that can hold limited weight, want max value
# input: list of tuples
# output: max value bag can hold


def max_duffel_bag_value(cakes, capacity):
    # trying to find combinations that add up to capacity, while maximizing value
    # greedy algo, keep track of highest value up to capacity of bag
    max_values= [0]*(capacity+1)
   for current_capacity in xrange(capacity +1):
       current_max_value = 0
       for weight, value in cakes:
           if weight <= current_capacity:
               max_values[current_capacity] =


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)