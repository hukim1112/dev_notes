# Sometimes you want to wrap your function before and after with some codes.
# Then you should use decorator, python programming pattern.
# ref : https://www.python-course.eu/python3_decorators.php
def our_decorator(func):

    def function_wrapper(x):
        print("Before calling : {}".format(func.__name__))
        func(x)
        print("After calling : {}".format(func.__name__))

    return function_wrapper


def foo(x):
    assert x.__class__ == int
    print("x + 10 is ", x + 10)


@our_decorator
def foo2(x):
    assert x.__class__ == int
    print("x + 20 is ", x + 20)


def main():

    wrapped_foo = our_decorator(foo)
    wrapped_foo(5)

    '''the function foo2 is wrapped with our_decorator function. It just need the decorator( @ ) with a wrapping function above the definition part of foo2 which you want to wrap up with the wrapping funciton.'''
    foo2(5)


if __name__ == '__main__':
    main()
