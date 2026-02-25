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

def skript_6():
    print("Запущен скрипт 6")
    text = input("Введите предложение: ")

    unique_chars = []

    for char in text:
        if text.count(char) == 1:
            unique_chars.append(char)

    print("Символы, встречающиеся один раз:")
    print("".join(unique_chars))

def skript_7():
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

def skript_8():
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

def skript_9():
    print("Запущен скрипт 9")