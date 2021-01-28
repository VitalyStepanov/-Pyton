def sum_my_func():
    res = 0
    while True:
        numbers = input('Введите чила через пробел или * для выхода из программы: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или *')
        print(f' Сумма равна: {res}')


print(sum_my_func())
