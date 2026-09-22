# Without Built in function:

Test_case = int(input())

for i in range(Test_case):
    count = 0
    array = list(map(int,input().split()))
    for i in array:
        if i == 0:
            count += 1
    if count == 0:
        print("No absentees")
    else:
        print(count,"Student absent")
        
        
# With Built in function:
Test_case = int(input())

for i in range(Test_case):
    array = list(map(int,input().split()))
    if sum(array) == len(array):
        print("No abdentees")
    else:
        print(len(array)-sum(array),"Students Absent")


# With Count function:

Test_case = int(input())

for i in range(Test_case):
    array = list(map(int,input().split()))
    if array.count(0) == 0:
        print("No absentees")
    else:
        print(array.count(0),"Student Absent")

        

