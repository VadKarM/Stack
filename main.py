from balance_brackets import balance_brackets


def balance():
    user_input = input("Введите строку со скобками: ")

    result = balance_brackets(user_input)
    status = "Сбалансированно" if result else "Несбалансированно"

    print(f"'{user_input}' -> {status}")


if __name__ == "__main__":
    balance()





