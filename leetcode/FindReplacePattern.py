"""
Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
"""

def findAndReplacePattern(words, pattern):
    def match(word):
        P = {}
        print "for word --", word
        for x, y in zip(pattern, word):
            print P.setdefault(x, y) , y , P
            if P.setdefault(x, y) != y:
                return False
        print  P 
        return len(set(P.values())) == len(P.values())
    return filter(match, words)


words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

print findAndReplacePattern(words, pattern)
