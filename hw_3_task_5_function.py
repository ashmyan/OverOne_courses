def fact2(n):
    summ_p = 1
    summ_ot = 1
    if n > 0:
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                summ_p *= i
            print(summ_p)
        else:
            for j in range(1, n + 1, 2):
                summ_ot *= j
            print(summ_ot)
    else:
        print("error")

fact2(7)