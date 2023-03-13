#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    count1 = 0
    list1 = []
    if (len_a == 2 or len_a > 2) and (len_b == 2 or len_b > 2):
        for pair in zip(tuple_a, tuple_b):
            if (count1 < 2):
                list1.append(sum(pair))
            count1 += 1
        return (tuple(list1))
    else:
        added_zero = (0, 0)
        tuple_a = tuple_a + added_zero
        tuple_b = tuple_b + added_zero
        for pair in zip(tuple_a, tuple_b):
            if (count1 < 2):
                list1.append(sum(pair))
            count1 += 1
        return (tuple(list1))
