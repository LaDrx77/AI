"""Лабораторна робота №6: демонстрація трьох парадигм програмування."""


def imperative_demo():
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for number in numbers:
        total += number
    print("Імперативна парадигма")
    print("Список:", numbers)
    print("Сума елементів:", total)
    return total


class Car:
    def __init__(self, model):
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print(f"{self.model} запущено.")

    def stop(self):
        self.running = False
        print(f"{self.model} зупинено.")


def oop_demo():
    print("\nОб'єктно-орієнтована парадигма")
    car = Car("Tesla Model S")
    car.start()
    print("Стан running після start():", car.running)
    car.stop()
    print("Стан running після stop():", car.running)
    return car.running


def functional_demo():
    numbers = [2, 4, 6, 8, 10]
    squares = list(map(lambda x: x ** 2, numbers))
    even_over_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
    print("\nФункціональна парадигма")
    print("Список:", numbers)
    print("Квадрати (map):", squares)
    print("Парні > 5 (filter):", even_over_five)
    return squares, even_over_five


def main():
    total = imperative_demo()
    final_running = oop_demo()
    squares, filtered = functional_demo()

    # Контрольні перевірки результатів.
    assert total == 150
    assert final_running is False
    assert squares == [4, 16, 36, 64, 100]
    assert filtered == [6, 8, 10]
    print("\nПеревірка: 4/4 PASS")


if __name__ == "__main__":
    main()
