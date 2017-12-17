def chain(*args):
    """
    Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей
    Обобщим до конкатенации n кортежей(вообще любых iterable) с помощью генератора и функции,
    возвращающей объект конкатенации (conc(*args, object_type))

    """
    for item in args:
        try:
            if iter(item):
                yield from item
        except TypeError:
            yield item

def conc(*args, object_type):

    a = object_type(chain(*args))
    return a

#test
# print(conc((1,2,3),(3,4,5), object_type = tuple)) #[1,2,3,3,4,5]
# print(conc([10, 234, 54], 11, set([5, 3, 9, 40]), object_type = set)) #{3, 5, 40, 9, 10, 11, 234, 54}

