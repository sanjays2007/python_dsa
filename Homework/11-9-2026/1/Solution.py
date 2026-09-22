arr = [1,2,3,4,5]
n = int(input())

n = n%len(arr)
arr = arr[n:] + arr[:n]

print(arr)