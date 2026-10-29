def censor(text: str, word: str) -> str:
    return text.replace(word, "*")


print(censor("this hack is wack hack", "hack"))
