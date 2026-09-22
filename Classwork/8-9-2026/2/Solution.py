array = list(map(int,input().split()))
count = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] == array[j]:
            count += 1

if count == 0:
    print("Yes")
else:
    print("No")

#With set fuction
no_dup = set(array)

if len(array) == len(no_dup):
    print("Yes")
else:
    print("No")

#
res = "Yes"
dup = []
for i in array:
    if i not in dup:
        dup.append(i)
    else:
        res = "No"

print(res)