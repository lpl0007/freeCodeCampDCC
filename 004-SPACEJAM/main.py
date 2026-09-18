def space_jam(s):
    s = s.replace(" ", "").upper()
    t = ""
    for i in s:
        t += i + "  "
    return t[:len(t)-2]
