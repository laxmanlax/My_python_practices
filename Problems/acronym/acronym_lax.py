test=[]
def acronym(words):
    for word in words.split():
        for w in word.split('-'):
            test.append(w[0])
    return ''.join(w.upper() for w in test)
    #return ''.join(w[0].upper() for w in word.split("-") for word in words.split())
print acronym("First In, First Out")
