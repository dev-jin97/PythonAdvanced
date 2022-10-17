
# positional parameter

def my_func(a, b):
    print(a, b)


my_func(1, 2)


# default parameter
def message(title, contents="NOT"):
    print(title, contents)


message("Hello")


# keyword parmeter
def send_message(title, contents="Not"):
    print(title, contents)


send_message(title="Hello", contents="Wow")