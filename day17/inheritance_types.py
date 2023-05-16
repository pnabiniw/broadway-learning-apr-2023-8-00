# Multiple Inheritance

class B:
    a = 2


class A:
    a = 1


class C(A, B):
    pass


obj = C()
print(obj.a)


# Hierarchical Inheritance
class A:
    a = 1


class B(A):
    a = 2


class C(A):
    pass


obj = C()
print(obj.a)


# Multilevel Inheritance
class A:
    a = 1


class B(A):
    a = 2


class C(B):
    a = 3


class D(C):
    pass


obj = D()
print(obj.a)


# Hybrid Inheritance
class A:
    a = 1

class B:
    a = 2

class C(A, B):
    a = 3

class D(C):
    a = 4

class E(C):
    pass

print(E.mro())   # Method Resolution Order



class A:
    a = 1
    b = 1

class B(A):
    a = 2

class C(A):
    a = 3
    c = 2

class D(B, C):
    pass

print(D.mro())
obj = A()
print(obj.a)


