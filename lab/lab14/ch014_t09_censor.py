def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    # return text.replace(word, asterisks)
    ts = text.split()
    for t in range(ts):
        if t == word:
            

print(censor("reverse", "se"))