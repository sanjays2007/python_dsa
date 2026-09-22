try:
    n = int(input("Enter a value :"))
    a , b = 0 , 1

    for i in range(n):
        print(a)
        a , b = b , a + b


except Exception as e:
    print("Invalid Input")