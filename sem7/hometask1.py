def rythm_check(phrase):
    volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ю', 'я']
    parts = phrase.split()#разделяет строку на список подстрок (разделить пробел по умолчанию)
    result = list()
    for item in parts:
        k = 0
        for letter in item:
            if letter in volwes:
                k += 1
        result.append(k)
    if len(set(result)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
song = input("Введите текст стихотворения: ")
rythm_check(song)