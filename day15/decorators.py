import time

def decorate_me(func):  # func => message
    def inner_func():
        print("I'm a decorated function")
        func()
    return inner_func


def to_upper(func):
    def inner_func():
        value = func()
        return value.upper()
    return inner_func


def exec_time(func):
    def inner_func():
        start = time.time()
        a = func()
        end = time.time()
        print(f"Execution time is {end-start}")
        return a
    return inner_func


def login_required(func):
    def inner_function():
        pw = input("Enter the password ")
        if pw == "123":
            return func()
        else:
            return "Invalid Password"
    return inner_function
