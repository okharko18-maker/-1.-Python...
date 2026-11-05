"""МКР. Завдання 03: Статистика слів."""

def solve(text: str) -> str:
    words = text.split()

    count = len(words)

    if words:
        longest = max(words, key=len)
    else:
        longest = "-"

    capitalized = sum(1 for word in words if word[0].isupper())

    return (
        f"Слів: {count}\n"
        f"Найдовше: {longest}\n"
        f"З великої літери: {capitalized}"
    )