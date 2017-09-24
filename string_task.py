def verbing(s):
  if len(s) < 3:
    return s
  else:
    if s[-3:] == 'ing':
      return s + 'ly'
    else:
      return s + 'ing'


def not_bad(s):
  nt = s.find("not")
  bad = s.find("bad")
  if nt != -1 and bad != -1 and  nt < bad:
    s = s[:nt] + 'good' + s[bad+3:]
  return s

