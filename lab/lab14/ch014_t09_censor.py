def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    # return text.replace(word, asterisks)
    ts = text.split()
    for i in range(ts):
        if ts[i] == word:
            ts[i] = asterisks
    ts.
            

print(censor("reverse", "se"))