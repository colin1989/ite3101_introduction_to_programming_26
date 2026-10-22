def censor(text: str, word: str) -> str:
    idx = text.index(word)
    for i in range(len(word)):
        text[i] = '*'
