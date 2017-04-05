def detect_anagrams(list01, list02):
    match=""
    for i in list02.split():
        if "".join(sorted(list01)).lower()== "".join(sorted(i)).lower():
            match=i
    return match

print detect_anagrams('master', 'Stream pigeon maters')
