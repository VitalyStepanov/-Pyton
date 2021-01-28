def exe_2(**kwargs):
    return list(kwargs.values())


print(exe_2(name=input('Введите имя: '),
            s_name=input('Введите фамилию: '),
            b_date= int(input('Введите год рождения: ')),
            l_town=input('Введите адрес: '),
            email=input('Введите  email: '),
            tel=input('Введите номер телефона: ')))
