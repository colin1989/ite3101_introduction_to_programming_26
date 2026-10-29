def censor(text: str, word: str) -> str:
    text.replace(word, "*")
        


print(censor("this hack is wack hack", "hack"))
