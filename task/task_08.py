
"""МКР. Завдання 08: Порівняння наборів тегів."""


def compare_tags(first: list, second: list) -> dict:
    first_set = {tag.strip().lower() for tag in first if tag.strip()}
    second_set = {tag.strip().lower() for tag in second if tag.strip()}

    only_first = sorted(first_set - second_set)
    only_second = sorted(second_set - first_set)
    both = sorted(first_set & second_set)

    union = first_set | second_set

    if union:
        similarity = round(len(both) / len(union), 2)
    else:
        similarity = 0.0

    return {
        "only_first": only_first,
        "only_second": only_second,
        "both": both,
        "similarity": similarity
    }