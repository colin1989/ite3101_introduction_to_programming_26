def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    output = []
    for
    ts = text.split()
    for i, token in enumerate(ts):
        if token == word:
            ts[i] = asterisks
    return " ".join(ts)
