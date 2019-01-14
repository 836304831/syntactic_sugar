
from functools import reduce
from collections import Iterator


def dynamic_params(*args, **kwargs):
    print("******args**************")
    print("type:{}".format(type(args)))
    print("args:{}".format(args))

    print("*****kwargs***************")
    print("type:{}".format(type(kwargs)))
    print("kwargs:{}".format(kwargs))


def anonymous_function(xxx):

    return lambda xxx: xxx*2


def str_upper(str):
    return str.upper()


def reduce_add(x, y):
    return x + y


def higher_order_func_check():
    print("*******higher_order_func***********")
    str1 = 'hello'
    print("str1:{}".format(str1))
    str2 = map(str_upper, str1)
    print("str2 type:{}".format(type(str2)))
    print("str2:{}".format(list(str2)))

    str2 = map(lambda a: a.upper(), str1)
    print("str2 type:{}".format(type(str2)))
    print("str2:{}".format(list(str2)))


def reduce_check():
    print("********reduce*****************")
    result = reduce(reduce_add, [1, 2, 3, 4, 5])
    print("result:{}".format(result))

    result = reduce(lambda x, y: x*y, range(1, 6))
    print("result:{}".format(result))


def filter_check():
    print("***********filter************")
    odd_numbers = filter(lambda x: x%2 == 0, range(0, 20))
    print("odd_numbers type:{}".format(type(odd_numbers)))
    print(isinstance(odd_numbers, Iterator))
    print("odd_numbers:{}".format(list(odd_numbers)))


def anonymous_function_check():
    print("value:{}".format(anonymous_function(xxx=2)))


def dynamic_params_check():
    dynamic_params(1, 2, 3, a='a', b='b', c='c')

    args = [1, 2, 3]
    kwargs = {'a': 'a', 'b': 'b', 'c': 'c'}
    dynamic_params(*args, **kwargs)


if __name__ == "__main__":
    dynamic_params_check()
    anonymous_function_check()
    higher_order_func_check()
    reduce_check()
    filter_check()