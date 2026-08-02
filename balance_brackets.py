from stack import Stack


def balance_brackets(brackets_string):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = Stack()

    for char in brackets_string:
        if char in brackets:
            if stack.is_empty():
                return False

            top = stack.pop()
            if top != brackets[char]:
                return False

        elif char in '([{':
            stack.push(char)

    return stack.is_empty()

