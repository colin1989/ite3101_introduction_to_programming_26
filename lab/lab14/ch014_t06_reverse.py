def reverse(text: str) -> str:
    o = ""
    # range(start, stop, step)
    for i in range(len(text) - 1, -1, -1):
        o += text[i]
    return o
    # return "".join(reversed(text))
    # o = ""
    # for t in range(len(text)):
    #     t = len(text) - 1 - t
    #     o += text[t]
    # return o
