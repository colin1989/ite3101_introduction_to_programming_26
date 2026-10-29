def censor(text: str, word: str) -> str:
    wl = len(word)
    idx = text.index(word)
    while idx >= 0:
        for i in wl:
            
    return text.replace(word, "*")


print(censor("this hack is wack hack", "hack"))
