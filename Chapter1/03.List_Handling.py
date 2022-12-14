# List Handling

# Delete data in List
fruits = ["apple", "orange", "mango"]
fruits.remove("mango") # delete "mango" data in List
# or
del fruits[2] # target index

# List sort
numbers = [3, 5, 1, 2, 6]
numbers.sort(reverse=True)
print(numbers)

# enumerate
titles = ["check!", "check,too!", "checkkkkk~"]

for idx, title in enumerate(titles):
    print((idx + 1), title)