import functools

### Playground


def function_that_return_decorator(lmd):
    def real_decorator(my_func_pnt):
        # https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
        @functools.wraps(my_func_pnt)
        def wrapper(my_func_arg):  # Arguments of my_func
            if lmd(my_func_arg):
                my_func_pnt(0)
            else:
                my_func_pnt(my_func_arg)

        return wrapper

    return real_decorator


def has_preferred_number(preferred_number):
    return lambda my_func_arg: my_func_arg == preferred_number


@function_that_return_decorator(has_preferred_number(50))
def my_func(x):
    print(x)
    pass


my_func(555)
my_func(50)


### Simulate with classmethod


class ValidatorException(Exception):
    pass


def validator(cond, exception: ValidatorException):
    def decorator(fn_pnt):
        @functools.wraps(fn_pnt)
        def wrapper(cls, *args):  # Arguments of my_func
            if not cond(*args):
                raise exception
            fn_pnt(cls, *args)

        return wrapper

    return decorator


def is_intersect_ids(target_ids):
    return lambda ids: set(ids).intersection(target_ids)


class MyClass:
    # @validator must be under @classmethod if we want to access cls or self argument
    @classmethod
    @validator(
        is_intersect_ids([6, 7, 8, 9]),
        ValidatorException("input ids is not collapse with expected ids"),
    )
    def func_1(cls, ids):
        print(ids)


try:
    MyClass.func_1([1, 2, 3, 4, 5])
except ValidatorException as e:
    print(e)

try:
    MyClass.func_1([5, 6, 7])
except ValidatorException as e:
    print(e)
