"""МКР. Завдання 10: Ледачі вікна й серії."""

from collections import deque


def windows(items, k: int):
    if k <= 0:
        raise ValueError("k має бути додатним")

    iterator = iter(items)
    window = deque()

    for _ in range(k):
        try:
            window.append(next(iterator))
        except StopIteration:
            return

    yield tuple(window)

    for item in iterator:
        window.popleft()
        window.append(item)
        yield tuple(window)


def run_lengths(items):
    iterator = iter(items)

    try:
        current = next(iterator)
    except StopIteration:
        return

    count = 1

    for item in iterator:
        if item == current:
            count += 1
        else:
            yield (current, count)
            current = item
            count = 1

    yield (current, count)


def best_window(values: list, k: int):
    if k <= 0:
        raise ValueError("k має бути додатним")

    best = None

    for start, window in enumerate(windows(values, k)):
        total = sum(window)

        if best is None or total > best[1]:
            best = (start, total)

    return best
