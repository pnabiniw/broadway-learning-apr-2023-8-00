# Arbitrary Arguments (Args and Kwargs)
# Args => Arguments
# Kwargs => Keyword Arguments
def addition(*args):
    return sum(args)


result = addition(1, 2, 3, 4, 5)
print(result)


def addition(**kwargs):
    return sum(kwargs.values())


result = addition(a=1, b=2, c=3, d=4)
print(result)

# *args and **kwargs are like stretchable arguments. We can
# send random number of parameters in these arguments during
# a function call


### Order of arguments in a function ####
def order_test(a, b, c, d=2, e=3, f=5, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)


order_test(10, 12, 5, 7, 9, 4, 5, 6, 7, 10, p=1, q=2, r=3)
