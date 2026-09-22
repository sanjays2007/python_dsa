arr = list(map(int,input().split()))
for i in range(len(arr)):
    arr.append(arr[-i-1])
    arr.remove(arr[-i-2])

print(arr)