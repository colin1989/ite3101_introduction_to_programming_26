def reverse(text: str) -> str:
    o = ""
    for t in range(len(text)):
        print("t : %s, text : %s" % t, text[t])
        o += text[t]
    return o

reverse("reverse")