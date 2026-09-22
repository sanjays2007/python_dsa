Test_case = int(input())

for i in range(Test_case):
    print("T",i+1)
    array = list(map(int,input().split()))
    even_arr = []
    odd_arr = []
    for num in array:
        if num%2 == 0:
            even_arr.append(num)
        else:
            odd_arr.append(num)

    if even_arr == []:
        print("Even Average : 0.00")
    else:      
        print("Even Average {:.2f}".format(sum(even_arr)/len(even_arr)))

    if odd_arr == []:
        print("Odd Average : 0.00")
    else:
        print("Odd Average {:.2f}".format(sum(odd_arr)/len(odd_arr)))
    