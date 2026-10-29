def censor(text: str, word: str) -> str:
    asterisks = '*' * len(word)
    # return text.replace(word, asterisks)
    ts = text.split()
    for i in range(ts):
        if t[i] == word:
            t[i] = asterisks
    
            

print(censor("reverse", "se"))