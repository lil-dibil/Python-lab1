import scripts

# Словарь соответствия номера и функции
tasks = {
    1: scripts.skript_1,
    2: scripts.skript_2,
    3: scripts.skript_3,
    4: scripts.skript_4
}

def show_menu():
    print("\nВыберите скрипт (1-16):")

while True:
    show_menu()

    try:
        choice = int(input("Введите номер: "))

        if choice == 0:
            print("Выход...")
            break

        if choice in tasks:
            tasks[choice]()
        else:
            print("Ошибка: Такого скрипта нет.")

    except ValueError:
        print("Ошибка: Введите число.")
