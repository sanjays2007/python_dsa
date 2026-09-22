# arr = list(map(int,input().split()))

arr = list(input().split())
occerence = {}

for i in arr:
    if i not in occerence.keys():
        occerence[i] = 0

    occerence[i] += 1

print(occerence)