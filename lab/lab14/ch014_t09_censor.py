def censor(text: str, word: str) -> str:
    asterisks = ''
    for _ in range(len(word)):
        asterisks += '*'

    return text.replace(word, asterisks)


print(censor("this hack is wack hack", "hack"))
