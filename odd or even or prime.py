for x in range(1, 101):
    if x % 2 == 0:
        print(x)
        print("these are the even numbers")
    for x in range(1, 101):
        if x % 2 != 0:
            print(x)
            print("these are the odd numbers")
for Number in range(1, 101):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if Number % i == 0:
            count = count + 1
            break
    if count == 0 and Number != 1:
        print(" %d" % Number, end="  ")
        print("these are the prime numbers")
