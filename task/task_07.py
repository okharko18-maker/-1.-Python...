"""МКР. Завдання 07: Лічильник із замиканням."""


def make_counter(step: int):
    count = 0

    def counter():
        nonlocal count
        count += step
        return count

    return counter


def apply_n(f, n: int) -> list:
    result = []

    for _ in range(n):
        result.append(f())

    return result
