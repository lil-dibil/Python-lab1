import scripts

# Словарь соответствия номера и функции
tasks = {
    1: scripts.skript_1,
    2: scripts.skript_2,
    3: scripts.skript_3,
    4: scripts.skript_4,
    5: scripts.skript_5,
    6: scripts.skript_6,
    7: scripts.skript_7,
    8: scripts.skript_8,
    9: scripts.skript_9,
    10: scripts.skript_10,
    11: lambda: print(list(scripts.frange(0, 6, 0.2))),
    12: lambda: [print(frame) for frame in scripts.get_frames(list(range(20)), size=8, overlap=0.5)],
    13: lambda: [print(data) for data in scripts.extra_enumerate([1, 3, 4, 2])],
    14: lambda: print(scripts.get_pages()),
    15: lambda: scripts.plot_signal([10, 20, 15, 30, 25]),
    16: lambda: scripts.football_groups()
}


def show_menu():
    print("\nВыберите скрипт (1-16), 0 — выход:")


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
