#for integer

arr = list(map(int,input().split()))
target = int(input())

# arr = [1,2,3,1,2,1,3,4]
# target = 1

count = 0
for x in arr:
    if x == target:
        count += 1

print(count)

