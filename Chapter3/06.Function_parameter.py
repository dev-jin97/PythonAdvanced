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


# 위치 가변 매개 변수
def print_fruits(*args):
    print(args)


print_fruits("apple", "banana")


# 키워드 가변 매개변수
def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{{key : value}}")


print_dict(hello="nice to meet you")


# 매개변수 작성순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(title, content, *tags):
    print(title)
    print(content)
    print(tags)


post_info(
    "my_tag",
    "Hello world",
    "#Hi",
    "#Hello",
    "#CodeDefiner"
)

# Lamda 함수
minus_one = lambda a: a - 1

print(minus_one(10))

# Lamda 함수 안에서 if문
is_positive = lambda a: True if a > 0 else False

print(is_positive(-1))