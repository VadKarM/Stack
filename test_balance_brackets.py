from balance_brackets import balance_brackets


def test_balance():
        test_strings = [
                "(((([{}]))))",
                "[([])((([[[]]])))]{()}",
                "{{[()]}}",
                "}{}",
                "{{[(])]}}",
                "[[{())}]"
        ]

        for s in test_strings:
                result = balance_brackets(s)
                status = "Сбалансированно" if result else "Несбалансированно"
                print(f"'{s}' -> {status}")


if __name__ == "__main__":
    test_balance()