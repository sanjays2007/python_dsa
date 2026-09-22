#for string

arr = input()
target = input()

# arr = "Hello"
# target = "l"

count = 0
for x in arr:
    if x == target:
        count += 1

print(count)

