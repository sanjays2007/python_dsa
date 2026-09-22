array = list(map(int,input("Enter the array :").split()))
Odd_element = []

for i in range(len(array)-2):
    Odd_element.append(array[i+1])

print(Odd_element)