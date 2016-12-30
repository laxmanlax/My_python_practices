def detect_anagrams(w, poss):
    return filter(lambda p: tst_anagram(w, p), poss)

def tst_anagram(w, p):
    return  w.lower() != p.lower() and ''.join(sorted(w.lower())) == ''.join(sorted(p.lower()))
