def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    return text.replace(word, asterisks)

censor("reverse", "se")