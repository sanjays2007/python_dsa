#Case-1
Test_case = int(input())

for i in range(Test_case):
    array = input()
    print("Attendance :{:.2f}".format(array.count("1")/(array.count("1")+array.count("0")) * 100))

#Case-2
Test_case = int(input())

for i in range(Test_case):
    array = input()
    print(array.count("0"),"Student Absent out of",array.count("1")+array.count("0")) if array.count("0") != 0 else print("No Absentees")
    print("Attendance :{:.2f}".format(array.count("1")/(array.count("1")+array.count("0")) * 100))