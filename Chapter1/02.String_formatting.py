
# What if there is no string formatting?

name = "기준"
duration = 7

message = name + "님 수강기간이 " + duration + "일 남았습니다." # duration is need to String formatting
print(message)

# Use a String Formatting
message_format = f"{name}님 수강기간이 {duration}일 남았습니다."

# Use a format method
case_1 = "Hello {0}{1}{2}".format("apple", "banana", "pen")

case_2 = "Hello {1}{0}{2}".format("apple", "banana", "pen")

case_3 = "Hello {}{}{}".format("apple", "pen", "melon")


# Use a f-string
name1 = "apple"
name2 = "pineapple"
name3 = "pen"

str_1 = f"Hello {name1}{name2}{name3}"

