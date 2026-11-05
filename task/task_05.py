
"""МКР. Завдання 05: Частоти символів."""


def solve(text: str) -> str:
    text = text.lower()

    frequencies = {}

    for char in text:
        if not char.isspace():
            frequencies[char] = frequencies.get(char, 0) + 1

    if not frequencies:
        return "Порожній текст"

    sorted_chars = sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )

    result = []

    for char, count in sorted_chars[:5]:
        result.append(f"{char}: {count}")

    result.append(f"Різних символів: {len(frequencies)}")

    return "\n".join(result)