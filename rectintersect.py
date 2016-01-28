# given 2 input rectangles, find intersection rectangle
#   my_rectangle = {
#
#     # coordinates of bottom-left corner:
#     'x': 1,
#     'y': 5,
#
#     # width and height
#     'width': 10,
#     'height': 4,
#
# }
# start off with finding all the corners, then determine overlap

import collections


def find_overlap(x1,x2, width1, width2):
    x1 = range(x1, x1+width1+1)
    x2 = range(x2, x2+width2+1)
    overlap = list((collections.Counter(x1) & collections.Counter(x2)).elements())
    return overlap


def find_rect_overlap(rect1, rect2):
    x_overlap = find_overlap(rect1['x'], rect2['x'],rect1['width'], rect2['width'])
    y_overlap = find_overlap(rect1['y'], rect2['y'],rect1['height'], rect2['height'])
    return {
        'x': x_overlap[0],
        'y': y_overlap[0],
        'width': len(x_overlap),
        'height': len(y_overlap)
    }

rect1 = {'x':3, 'y':1, 'width':4, 'height':5}
rect2 = {'x':5, 'y':3, 'width':4, 'height':2}
print find_rect_overlap(rect1,rect2)