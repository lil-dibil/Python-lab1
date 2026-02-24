def skript_1():
    print("Запущен скрипт 1")
    try:
        number = float(input("Введите вещественное число: "))

        if number < 0:
            raise ValueError("Отрицательное число")

        rub = int(number)
        kop = round((number - rub) * 100)

        print(f"{rub} руб. {kop:02d} коп.")

    except ValueError:
        print("Некорректный формат!")

def skript_2():
    print("Запущен скрипт 2")
    numbers = [1, 3, 5, 7, 9] # тест

    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))

    print(is_increasing)

def skript_3():
    print("Запущен скрипт 3")
    try:
        card = input("Введите номер карты (16 цифр): ")

        if not (card.isdigit() and len(card) == 16):
            raise ValueError

        hidden = f"{card[:4]} **** **** {card[-4:]}"
        print(hidden)

    except ValueError:
        print("Некорректный номер карты!")

def skript_4():
    print("Запущен скрипт 4")
    text = input("Введите текст: ")

    words = text.split()

    long_words = [w for w in words if len(w) > 7]
    medium_words = [w for w in words if 4 <= len(w) <= 7]
    short_words = [w for w in words if len(w) < 4]

    print("Длинные слова (>7):", long_words)
    print("Средние слова (4-7):", medium_words)
    print("Короткие слова (<4):", short_words)

def skript_5():
    print("Запущен скрипт 5")