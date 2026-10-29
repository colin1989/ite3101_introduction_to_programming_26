def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    # return text.replace(word, asterisks)
    ts = text.split()
    for i in range(len(ts)):
        if ts[i] == word:
            ts[i] = asterisks
    return "".join(ts)


print(censor("this hack is wack hack", "hack"))
print(censor("reverse", "se"))

