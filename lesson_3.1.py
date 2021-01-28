
def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На 0 делитть нельзя'
    except ValueError:
        return 'No value'

print(exe_1((int(input('Введите первое число: '))), (int(input('Введите второе число: ')))))