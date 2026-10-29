def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    output = []
    for token in text.split():
        if token == word:
            output.append(asterisks)
        else:
            output.append(token)
    return " ".join(output)
