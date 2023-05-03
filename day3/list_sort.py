l = [(2, 3), (1, 1), (4, 2), (5, 5), (2, 4)]

# Arrange the above list based on the second element of each
# item inside the list
# Result should be [(1, 1), (4, 2), (2, 3), (2, 4), (5, 5)]


def get_second_item(d):
    return d[1]


l.sort(key=get_second_item)
print(l)


a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]


def sort_based_on_last(data):
    return data[-1]


a.sort(key=sort_based_on_last)
print(a)
