def reverse(text: str) -> str:
    o = ""
    for t in range(len(text) - 1, 0):
        o += text[t]
    return o