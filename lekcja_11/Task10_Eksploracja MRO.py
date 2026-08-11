class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


print(F.mro())