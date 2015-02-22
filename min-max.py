import collections
import types
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args)==1:
        if isinstance(args[0], collections.Iterable):
            if key:
                min_val=args[0][0]
                for arg in args[0]:
                    if key(arg)<key(min_val): min_val=arg
                return min_val
            if isinstance(args[0],types.GeneratorType) or isinstance(args[0],set):
                args = list(args[0])
                min_val = args[0]
                for arg in args:
                    if arg<min_val: min_val=arg
                return min_val
            min_val=args[0][0]
            for arg in args[0]:
                if arg<min_val: min_val=arg
            return min_val
    if key:
        min_val=args[0]
        for arg in args:
            if key(arg)<key(min_val): min_val=arg
        return min_val
    min_val=args[0]
    for arg in args:
        if arg<min_val: min_val=arg
    return min_val


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args)==1:
        if isinstance(args[0], collections.Iterable):
            if key:
                max_val=args[0][0]
                for arg in args[0]:
                    if key(arg)>key(max_val): max_val=arg
                return max_val
            if isinstance(args[0],types.GeneratorType) or isinstance(args[0],set):
                args = list(args[0])
                max_val = args[0]
                for arg in args:
                    if arg>max_val: max_val=arg
                return max_val
            max_val=args[0][0]
            for arg in args[0]:
                if arg>max_val: max_val=arg
            return max_val
    if key:
        max_val=args[0]
        for arg in args:
            if key(arg)>key(max_val): max_val=arg
        return max_val
    max_val=args[0]
    for arg in args:
        if arg>max_val: max_val=arg
    return max_val


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print max(filter(str.isalpha,"@v$e56r5CY{]"))
    print max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1])