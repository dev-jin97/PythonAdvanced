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


# map 함수
# 사용이유
# 기존 리스트를 수정해서 새로운 리스트를 만들 때

# 사용방법
# map(함수, 순서가 있는 자료형)
print(list(map(int, ["3", "4", "5", "6"])))

blank_word = ["    shell", "   hello    "]

print(list(map(lambda x: x.strip(), blank_word)))


# filter 함수
# 사용이유
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때


# 사용방법
# filter(함수, 순서가 있는 자료형)
def func(x):
    return x < 0


print(list(filter(func, [-3, -2, -1, 0, 1])))


print(list(filter(lambda x: len(x) <= 3, ["abc", "abcd", "abcde", "bnc"])))



