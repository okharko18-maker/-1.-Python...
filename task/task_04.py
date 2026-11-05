"""МКР. Завдання 04: Конвертер температур."""


def solve(value: str, scale: str) -> str:
    value = value.strip()
    scale = scale.strip().upper()

    if scale not in ("C", "F", "K"):
        return "Помилка: некоректні дані"

    try:
        if not value or value in ("-", ".", "-."):
            return "Помилка: некоректні дані"

        number = float(value)

        if not any(char.isdigit() for char in value):
            return "Помилка: некоректні дані"

        if value.count(".") > 1:
            return "Помилка: некоректні дані"

        if value.startswith(".") or value.endswith("."):
            return "Помилка: некоректні дані"

        if value.startswith("-."):
            return "Помилка: некоректні дані"

    except ValueError:
        return "Помилка: некоректні дані"

    if scale == "C":
        celsius = number
    elif scale == "F":
        celsius = (number - 32) * 5 / 9
    else:
        celsius = number - 273.15

    if celsius < -273.15:
        return "Помилка: нижче абсолютного нуля"

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    return (
        f"C: {celsius:.1f}\n"
        f"F: {fahrenheit:.1f}\n"
        f"K: {kelvin:.1f}"
    )