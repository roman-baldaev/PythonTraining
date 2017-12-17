from basic import chain

def sumall(*args):
    """
    Написать функцию, которой можно передавать аргументы либо списком/кортежем,
    либо по одному. Функция производит суммирование всех аргументов.
    Решим задачку с помощью генератора chain (не привыкать)

    """
    sum = 0
    gen = chain(*args)
    for item in gen:
        sum += item
    return sum

# test
# print(sumall([1,2,3], [5, 1], 10, (5,6,1,4))) #38


def addition(number):
    """
    Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
    Написать варианты с обычной "внутренней" и анонимной lambda-функцией.

    """
    def inner(plus):
        return number + plus
    return inner

# test
# add5 = addition(5)
# print(add5(8)) #13


def addition_lambda(number):
    """
    Вариант с lambda-функцией

    """
    return lambda x: number + x

# test
# add8 = addition_lambda(8)
# print(add8(10))
# add1000 = addition_lambda(1000)
# print(add1000(1111))


def addition_range(start = 0, stop = 0, step = 1):
    """
    Написать фабрику, аналогичную предыдущей, но возвращающей список таких функций

    """
    list_function = []
    if step == 0:
        raise ValueError('Step can`t be null')

    if (start > stop and step > 0):
        start, stop = stop, start

    for i in range(start, stop, step):
        list_function.append(addition_lambda(i))
    return list_function

# test
# a = addition_range(100, step = 2)
# for func in a:
#     print(func(-2)) #-2 0 2 4 6 8 ... etc


def mymap(*functions, args):
    """Написать аналог map:

        первым аргументом идет либо функция, либо список функций
        вторым аргументом — список аргументов, которые будут переданы функциям
        полагается, что эти функции — функции одного аргумента

    """
    gen = chain(*functions)
    result = [tuple(func(i) for i in args) for func in gen]
    return result

#test
# a = addition_range(1,10,2)
# print(mymap(a, args = [1,2,3])) #[(2, 3, 4), (4, 5, 6), (6, 7, 8), (8, 9, 10), (10, 11, 12)]


