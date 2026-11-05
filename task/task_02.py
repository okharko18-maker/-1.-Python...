"""МКР. Завдання 02: Таблиця множення."""


def solve(n: str) -> str:
    n = n.strip()

    try:
        number = int(n)
    except ValueError:
        return "Помилка: n має бути цілим від 1 до 12"

    if number < 1 or number > 12:
        return "Помилка: n має бути цілим від 1 до 12"

    result = []
    total = 0

    for k in range(1, 11):
        product = number * k
        result.append(f"{number} x {k} = {product}")
        total += product

    result.append(f"Сума: {total}")

    return "\n".join(result)
