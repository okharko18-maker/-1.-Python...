"""МКР. Завдання 01: Перевірка пароля."""

def solve(password: str) -> str:
    missing = []

    if len(password) < 8:
        missing.append("довжини")

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if not has_digit:
        missing.append("цифри")

    if not has_upper:
        missing.append("великої літери")

    if not has_lower:
        missing.append("малої літери")

    if missing:
        return "Не вистачає: " + ", ".join(missing)

    return "Пароль прийнято"