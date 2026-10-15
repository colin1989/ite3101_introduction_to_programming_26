vowels = ['a', 'e', 'i', 'o', 'u']
def anti_vowel(text: str) -> str:
    o = ""
    for t in text:
        if vowels.index(t) >= 0:
            
