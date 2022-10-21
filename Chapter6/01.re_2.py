import re

# 1. Group

str1 = '010-2345-5679'
result = re.match('.*', str1)
print(result.group())