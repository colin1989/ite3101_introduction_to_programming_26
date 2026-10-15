def reverse(text: str) -> str:
    o = ""
    for t in range(len(text) - 1):
        t = len(text) - 1 - t
        o += text[t]
    return o