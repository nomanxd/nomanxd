def verbing(s):
  if len(s) < 3:
    return s
  else:
    if s[-3:] == 'ing':
      return s + 'ly'
    else:
      return s + 'ing'


def not_bad(s):
    bad = s.find("bad") + 3
    nt = s.find("not")
    if nt > bad:
        s = s.replace(s[nt:bad:)], "good")
    return s
