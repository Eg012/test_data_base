f = [1, 2, 3, 4, 5, 7, 8, 12, 6]
count = 0
count2 = 0
for i in f:
    if f[0] % i > f[-1] % i:
        count +=1
        print("числа, которые делятся на первое число:", count)

    else:
        count2 += 1
        print("числа, которые делятся на второе число:", count2)
