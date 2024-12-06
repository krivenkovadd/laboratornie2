import doctest

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 512)
        >>> book.get_info()
        'Книга "Мастер и Маргарита" автора Михаил Булгаков, 512 страниц'
        """
        return f'Книга "{self.title}" автора {self.author}, {self.pages} страниц'

    def set_pages(self, new_pages: int) -> None:
        """
        Устанавливает новое количество страниц в книге.

        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 512)
        >>> book.set_pages(600)
        >>> book.pages
        600
        """
        if new_pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.pages = new_pages

class MiniCooper:
    def __init__(self, model: str, year: int, fuel_capacity: float, color: str):
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.color = color
        self.fuel_level = 0.0

    def get_info(self) -> str:
        """
        Возвращает информацию о Mini Cooper.

        >>> mini = MiniCooper("Cooper S", 2022, 40.0, "красный")
        >>> mini.get_info()
        'Mini Cooper Cooper S 2022 года выпуска, объем топливного бака 40.0 литров, цвет красный'
        """
        return f'Mini Cooper {self.model} {self.year} года выпуска, объем топливного бака {self.fuel_capacity} литров, цвет {self.color}'

    def refuel(self, amount: float) -> None:
        """
        Заправляет Mini Cooper указанным количеством топлива.

        >>> mini = MiniCooper("Cooper S", 2022, 40.0, "красный")
        >>> mini.refuel(20.0)
        >>> mini.fuel_level
        20.0
        """
        if amount <= 0:
            raise ValueError("Количество топлива для заправки должно быть положительным")
        remaining_capacity = self.fuel_capacity - self.fuel_level
        if amount > remaining_capacity:
            raise ValueError("Объем топливного бака недостаточен для заправки")
        self.fuel_level += amount

class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополняет счет на указанную сумму.

        >>> account = BankAccount("1234567890", "John Doe")
        >>> account.deposit(1000.0)
        >>> account.balance
        1000.0
        """
        if amount < 0:
            raise ValueError("Сумма для пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снимает указанную сумму со счета.

        >>> account = BankAccount("1234567890", "John Doe", 1000.0)
        >>> account.withdraw(500.0)
        >>> account.balance
        500.0

        >>> account.withdraw(1000.0)
        Traceback (most recent call last):
        ...
        ValueError: Недостаточно средств на счете
        """
        if amount < 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        >>> account = BankAccount("1234567890", "John Doe", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance

if __name__ == "__main__":
    doctest.testmod()
