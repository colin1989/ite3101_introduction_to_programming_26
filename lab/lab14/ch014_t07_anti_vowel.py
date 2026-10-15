vowels = ['a', 'e', 'i', 'o', 'u']
def anti_vowel(text: str) -> str:
    o = ""
    for t in text:
        if t in vowels:
            o += t
    return o
