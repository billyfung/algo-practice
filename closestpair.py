# finding closest pair in list of numbers
import itertools
import collections


def closest_pair(lst):
    min_pair = collections.defaultdict(list)
    min_distance = float("inf")
    for x,y in itertools.combinations(lst, 2):
        distance = abs(x-y)
        if distance <= min_distance:
            min_pair[distance].append('{} {}'.format(x,y))
            min_distance = distance
    return min_pair[min(min_pair)]

input = [10,-30,30,-20,40,5230,-40,520,420,100, 50, -50, 110]
print(closest_pair(input))