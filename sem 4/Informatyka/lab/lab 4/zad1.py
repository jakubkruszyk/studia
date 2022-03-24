def suma(*args):
    # return sum(args)
    x = args[0]
    for num in args[1:]:
        x += num
    return x


print(suma("test", "2"))
print(suma(1, 2, 3, 4))


def test(a, b):
    print(a + b)


print(test(a="a", b="b"))


def test2(**kwargs):
    print(kwargs)


kw = {'a': 1, 'b': 2, 'c': 3}

test2(**kw)
test2(a=1, b=2, c=3)
