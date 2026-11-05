"""МКР. Завдання 06: Фільтр і статистика чисел."""


def solve(text: str) -> str:
    parts = text.split()

    if not parts:
        return "Помилка: немає чисел."

    numbers = []

    for part in parts:
        if part.startswith("-"):
            digits = part[1:]
        else:
            digits = part

        if not digits.isdigit():
            return f"Помилка: некоректний елемент: {part}"

        numbers.append(int(part))

    positive = [x for x in numbers if x > 0]
    negative = [x for x in numbers if x < 0]
    zeros = [x for x in numbers if x == 0]

    def group_stats(name, values):
        if not values:
            return f"{name}: немає"

        average = sum(values) / len(values)

        return (
            f"{name}: {len(values)} шт., "
            f"мін {min(values)}, макс {max(values)}, "
            f"середнє {average:.2f}"
        )

    return (
        group_stats("Додатні", positive) + "\n"
        + group_stats("Від'ємні", negative) + "\n"
        + f"Нулі: {len(zeros)}"
    )