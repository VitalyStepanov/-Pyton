def exe_4(x, y):
    return 1 / x ** abs(y)


print(exe_4(2, -2))


def exe_41(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


print(exe_4(2, -2))
