def reverse(text: str) -> str:
    o = ""
    for t in range(0, len(text) - 1):
        o += text[t]
    return o