n = int(input(""))
array = []

for i in range(n):
    element = int(input())
    array.append(element)

for i in range(len(array)):
    for j in range(i+1, len(array)):
        print((array[i],array[j]))

