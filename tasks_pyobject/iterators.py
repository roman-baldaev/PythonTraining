from copy import copy


def cycle(iterator):
    """
        Написать функцию-генератор cycle которая бы возвращала циклический итератор.

    """
    t = copy(iterator)

    while True:
        try:
            yield next(iterator)
        except StopIteration:
            iterator = copy(t)

# test
# a = iter([1,2,3])
# c = cycle(a)
# for i in range(99):
#     print(next(c))