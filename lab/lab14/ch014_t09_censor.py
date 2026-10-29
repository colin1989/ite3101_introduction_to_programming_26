def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    return text.replace(word, asterisks)


print(censor("this hack is wack hack", "hack"))
