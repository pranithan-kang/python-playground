import functools


def function_that_return_decorator(fn_decor_param):
    def real_decorator(my_func_pnt):
        @functools.wraps(my_func_pnt)
        def wrapper(my_func_arg):  # Arguments of my_func
            print(f"decorator_wrapper is called {fn_decor_param}")
            my_func_pnt(my_func_arg)
        return wrapper

    return real_decorator


class A:
    # https://www.geeksforgeeks.org/__new__-in-python/
    def __new__(cls):
        print("A.__new__ is called")
        cls.i = 0

        def fn_in_a(param: cls._PseudoClass):
            print(f"fn_in_a is called {param} {type(cls._PseudoClass)}")

        cls.fn_in_a = fn_in_a

        @function_that_return_decorator(cls._PseudoClass)
        def fn_in_a_with_decor(param: cls._PseudoClass):
            print(f"fn_in_a_with_decor is called {param} {type(cls._PseudoClass)}")

        cls.fn_in_a_with_decor = fn_in_a_with_decor

        return super(A, cls).__new__(cls)


class PseudoClass:
    def __init__(self, a):
        self.a = a

class B(A):
    _PseudoClass = PseudoClass
    i1 = 0

# This must be called to invoke A.__new__
B()

B.fn_in_a(PseudoClass(a=12))
B.fn_in_a_with_decor(PseudoClass(a=12))

b = B()
pass