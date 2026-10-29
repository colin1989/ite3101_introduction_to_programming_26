def censor(text: str, word: str) -> str:
    asterisks = '*'
    asterisks += '*'

    return text.replace(word, "*")


print(censor("this hack is wack hack", "hack"))
