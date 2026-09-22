nums = [4,3,2,7,8,2,3,1]

freq = {}
res = []

for i in nums:
    freq[i] = freq.get(i,0) + 1

for i in nums:
    if freq[i] > 1 and i not in res:
        res.append(i)

print(res)