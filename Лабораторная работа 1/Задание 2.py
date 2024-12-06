from task_1 import Book, MiniCooper, BankAccount

if __name__ == "__main__":
 book = Book('Мастер и Маргарита', 'Михаил Булгаков', 512)
 mini_cooper = MiniCooper('Cooper S', 2022, 40.0, 'Красный')
 bank_account = BankAccount('100500', 'Кривенкова Дарья', 1000.0)

    try:
     book.set_pages(-100)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     mini_cooper.refuel(-20.0)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     bank_account.withdraw(-500.0)
    except TypeError:
        print('Ошибка: неправильные данные')
