def verbing(s):
    if len(s) >= 3:
        if s[-3:1] == ing:
            s = s + "ly"
        else:
            s = s + "ing"
    return s


def not_bad(s):
    bad = s.find("bad")
    nt = s.find("not")
    if nt > bad:
        s = s.replace(s[nt]:s[bad]:1)
    return s
