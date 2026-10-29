# -*- coding: utf-8 -*-

NAME = "Calculator"
DESCRIPTION = "Performs basic arithmetic calculations."


def run(text):
    parts = text.split()

    if len(parts) != 3:
        return "Format: number operator number (example: 8 + 2)"

    try:
        a = float(parts[0])
        operator = parts[1]
        b = float(parts[2])

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                return "Error: Cannot divide by zero."
            result = a / b
        else:
            return "Unsupported operator. Use +, -, * or /."

        if result == int(result):
            return str(int(result))

        return str(result)

    except ValueError:
        return "Invalid numbers. Example: 8 + 2"


def test():
    assert run("8 + 2") == "10"
    assert run("9 - 4") == "5"
    assert run("6 * 3") == "18"
    assert run("8 / 2") == "4"
    assert run("8 / 0") == "Error: Cannot divide by zero."
    return True
