"""МКР. Завдання 09: Інвертований індекс слів."""


def build_index(docs: list) -> dict:
    index = {}

    punctuation = ".,!?;:\"'()"

    for doc_id, text in docs:
        words = text.split()

        for word in words:
            word = word.strip(punctuation).lower()

            if word:
                if word not in index:
                    index[word] = set()

                index[word].add(doc_id)

    return {
        word: sorted(doc_ids)
        for word, doc_ids in sorted(index.items())
    }


def search(index: dict, query: str) -> list:
    punctuation = ".,!?;:\"'()"

    required = []
    excluded = []

    for word in query.split():
        if word.startswith("-"):
            word = word[1:]
            word = word.strip(punctuation).lower()

            if word:
                excluded.append(word)
        else:
            word = word.strip(punctuation).lower()

            if word:
                required.append(word)

    if not required:
        return []

    result = None

    for word in required:
        if word not in index:
            return []

        ids = set(index[word])

        if result is None:
            result = ids
        else:
            result &= ids

    for word in excluded:
        if word in index:
            result -= set(index[word])

    return sorted(result)
