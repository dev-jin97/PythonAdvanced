# 1. replace

a= "Today's weather is cloudy.".replace("cloudy", "sunny")
print(a)

# 2. find

b = "Hello World".find("World")

print(b) # find a target index.

# 3. split
c = "Nikeshoes 265 x12122".split()
print(c)

d = "Nikeshoes,265,x12122".split(",")
print(d)

# 4. strip
e = "      hello       ".lstrip() # left strip
print(e)
f = "      hello       ".rstrip() # right strip
print(f)
g = "      hello       ".strip() # strip
print(g)


