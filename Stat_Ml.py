def fib(n):
    f1 = 0
    f2 = 1
    count = 0
    if n == 0:
        print("1")
    else:
        for i in range(n):
            # print(i)
            f = f1 + f2
            f1 = f2
            f2 = f
            count = count + 1
            print(f)



