def reverse(text: str) -> str:
    o = ""
    for t in range(len(text) - 1):
        t = len(text) - t
        print("t : %s, text : %s" % (t, text[t]))
        o += text[t]
    return o

reverse("reverse")