def verbing(s):
	if len(s) >= 3:
		if s[-3:1] == ing:
			s = s + "ly";
		else:
			s = s + "ing";
	return s;


def not_bad(s):
	bad = s.find("bad");
	not = s.find("not");
	if not > bad:
		s = s.replace(s[not]:s[bad]:1);
	return s;
