def skript_1():  # скрипт № 1
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


def skript_2():  # скрипт № 2
    print("Запущен скрипт 2")
    numbers = [1, 3, 5, 7, 9]  # тест

    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))

    print(is_increasing)


def skript_3():  # скрипт № 3
    print("Запущен скрипт 3")
    try:
        card = input("Введите номер карты (16 цифр): ")

        if not (card.isdigit() and len(card) == 16):
            raise ValueError

        hidden = f"{card[:4]} **** **** {card[-4:]}"
        print(hidden)

    except ValueError:
        print("Некорректный номер карты!")


def skript_4():  # скрипт № 4
    print("Запущен скрипт 4")
    text = input("Введите текст: ")

    words = text.split()

    long_words = [w for w in words if len(w) > 7]
    medium_words = [w for w in words if 4 <= len(w) <= 7]
    short_words = [w for w in words if len(w) < 4]

    print("Длинные слова (>7):", long_words)
    print("Средние слова (4-7):", medium_words)
    print("Короткие слова (<4):", short_words)


def skript_5():  # скрипт № 5
    print("Запущен скрипт 5")
    text = input("Введите предложение: ")

    words = text.split(" ")

    new_words = []

    for word in words:
        # Проверяем слово без запятой в конце
        clean_word = word.strip(",")

        if clean_word and clean_word[0].isupper():
            new_word = clean_word.upper()
        else:
            new_word = clean_word

        # Возвращаем запятую, если она была
        if word.endswith(","):
            new_word += ","

        new_words.append(new_word)

    result = " ".join(new_words)
    print(result)


def skript_6():  # скрипт № 6
    print("Запущен скрипт 6")
    text = input("Введите предложение: ")

    unique_chars = []

    for char in text:
        if text.count(char) == 1:
            unique_chars.append(char)

    print("Символы, встречающиеся один раз:")
    print("".join(unique_chars))


def skript_7():  # скрипт № 7
    print("Запущен скрипт 7")
    addresses = [
        "www.google",
        "www.youtube.com",
        "privet"
        "example.com",
        "www.github",
        "cool_site"
    ]

    new_addresses = [
        (("http://" + addr) if addr.startswith("www") else addr)
        for addr in addresses
    ]

    # Теперь проверяем окончание .com
    new_addresses = [
        (addr if addr.endswith(".com") else addr + ".com")
        for addr in new_addresses
    ]

    print("Исходный список:")
    print(addresses)

    print("Обработанный список:")
    print(new_addresses)


def skript_8():  # скрипт № 8
    print("Запущен скрипт 8")
    import random

    n = random.randint(1, 10000)
    print(f"Случайное n: {n}")

    array = [random.randint(0, 100) for _ in range(n)]

    # Находим ближайшую степень двойки
    power = 1
    while power < n:
        power *= 2

    zeros_to_add = power - n

    array.extend([0] * zeros_to_add)

    print(f"Размер после дополнения: {len(array)}")
    print(f"Ближайшая степень двойки: {power}")
    print(f"Добавлено нулей: {zeros_to_add}")


def skript_9():  # скрипт № 9
    print("Запущен скрипт 9")
    atm = {
        1000: 5,
        500: 5,
        100: 10,
        50: 10,
        10: 20
    }

    try:
        amount = int(input("Введите сумму: "))

        if amount <= 0:
            raise ValueError

        original_amount = amount
        result = []

        for bill in sorted(atm.keys(), reverse=True):
            count = min(amount // bill, atm[bill])

            if count > 0:
                result.append(f"{count}*{bill}")
                amount -= count * bill

        if amount != 0:
            print("Операция не может быть выполнена!")
        else:
            print(" + ".join(result))

    except ValueError:
        print("Некорректный ввод!")


def skript_10():  # скрипт № 10
    print("Запущен скрипт 10")
    password = input("Введите пароль: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        print("Слабый пароль")
    elif score <= 4:
        print("Средний пароль")
    else:
        print("Надежный пароль")


def frange(start, stop, step):  # скрипт № 11
    print("Запущен скрипт 11")
    current = start
    while current < stop:
        yield round(current, 10)  # защита от ошибок float
        current += step


def get_frames(signal, size, overlap):  # скрипт № 12
    print("Запущен скрипт 12")
    if not (0 <= overlap < 1):
        raise ValueError("overlap должен быть от 0 до 1")

    if size <= 0:
        raise ValueError("size должен быть больше 0")

    step = int(size * (1 - overlap))
    if step == 0:
        raise ValueError("Слишком большое перекрытие")

    for start in range(0, len(signal) - size + 1, step):
        yield signal[start:start + size]


signal = list(range(20))


def extra_enumerate(x):  # скрипт № 13
    print("Запущен скрипт 13")
