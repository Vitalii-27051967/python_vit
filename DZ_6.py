# Реализовать класс, который будет обеспечивать работу с банковским акканутом.
# Должна быть возможность задать начальное состояние аккаунта (сумма на счету, в том числе допустимо отрицательная).
# Поддерживаются операции:
# 1) Снятия наличных если после операции баланс остается полжительным или нулевым.
# 2) Начисление указанной суммы, но не более чем 10.000 денежных единиц.
# 3) Лог N проведенных транзакций (это число конфигурируется через конструктор и должно быть положительным
# целым числлом. N=0 означает, что логгирование выключено).


class Bank:

    def __init__(self):
        self.account = float(0)        # начальное состояние аккаунта
        self.test = ""                 # переменная для обработки по операциям
        self.log_add_sub = ""          # накопительная для лога транзакций

    def inp(self):
        self.test = input("Ввод сумы на счёт: ")
        self.account = float(bank.check_dig())
        bank.operations()

    def check_dig(self):                # если строка содержит цифры и может содержать точку или "-" в начале
        if self.test.replace(".", "").replace("-", "").isdigit():
            if "-" in self.test:
                if self.test.index("-") == 0 and self.test.count("-") == 1:
                    return self.test
                else:
                    bank.inp()
            else:
                return self.test

            ''' Выбор операции клавишами клавиатуры и переход на функции прибавления или вычитания '''

    def operations(self):  # operation
        print(f"Состояние счёта {self.account}")
        operation = input("Снятие \"-\" / Пополнение \"+\" \nДля выхода нажмите \"Enter\" ")
        if operation == "+":
            return bank.add()      # на п/п пополнения
        elif operation == "-":
            return bank.sub()      # на п/п снятия
        else:
            print("не корректный ввод или прекращение работы")
        return

    def add(self):  # addition
        self.test = input("Ввод суммы на пополнение (не более 10.000) ")
        k = abs(float(bank.check_dig()))
        if k <= 10.0:
            self.log_add_sub = self.log_add_sub + f"{self.account} add {self.account + k}*"
            self.account = self.account + k
        else:
            bank.operations()
        return bank.operations()

    def sub(self):  # subtraction
        if self.account < 0:
            return print("Изучите  \"Пособие по бродяжничеству\" \n"
                         " или погасите задолженность"), bank.operations()
        if float(self.account) == 0:
            return print("Вы не можете ничего снять. Состояние счёта = 0"), bank.operations()
        self.test = input(f"Ввод суммы на снятие (не более {self.account})  ")
        k = abs(float(bank.check_dig()))
        if k <= self.account:
            self.log_add_sub = self.log_add_sub + f"{self.account} sub {self.account - k}*"
            self.account = self.account - k
        return bank.operations()

    def log_transaction(self, trans):
        self.log_add_sub = self.log_add_sub + trans


bank = Bank()
bank.inp()

# Для проверки работы
print("_______________________________________")
print("Состояние счёта: ", bank.account)

print("_______________________________________")
print(bank.log_add_sub, "\n")
[print(i) for i in bank.log_add_sub.split("*")]

