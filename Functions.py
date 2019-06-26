# Функция "password" для генерации пароля

def password():
    import random

    # В качестве пароля будем использовать числа '0-9',
    # А также строчные и прописные буквы 'a-z'

    s1 = '0123456789'

    s2 = 'abcdefghijklmnopqrstuvwxyz'

    s3 = s2.upper()

    s4 = s1 + s2 + s3

    mix = list(s4)

    random.shuffle(mix)

    # Таким образом, был создан и случайно
    # Отсортирован список "mix" из выбранных символов

    # Теперь сгенерируем пароль,выбирая случайно
    # Символы из полученного списка "mix"

    pas = ''

    for i in range(16):
        x = random.choice(mix)
        pas = pas + str(x)

    # В итоге в переменной "pas" типа string находится
    # Случайно сгенерированный пароль из 16 символов

    return pas

# Функция "output" для преобразования входных параметров

def output(t):

    res = []
    l = len(t)

    for i in range(l):
        if ord(t[i]) == ord(' '):
            n = i
            break

    resource = t[:n]
    login = t[n + 1: l]

    res.append(resource)
    res.append(login)

    return res