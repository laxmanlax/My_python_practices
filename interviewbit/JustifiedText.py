"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces " " when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.
Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
"""
def justify(words, L):
    result = []
    last = 0

    for i in range(0,len(words)+3,3):
        temp = "".join(words[last:i])

        if len(temp) < L:
            space = L - len(temp)

            if (space)%2==0:
                left = space/2
                right = space - left 
            else:
                left = space/2 
                right = space - left 
        
            if len(words[last:i]) < 3:
                if len(words[last:i]) == 2:
                    r = space*" ".join(words[last:i])
                    result.append(r)
                if len(words[last:i]) == 1:
                    r = words[last:i][0]+space*" "
                    result.append(r)
            else:
                word = words[last:i]
                r = word[0]+left*" "+word[1]+right*" "+word[2]
                result.append(r)
        
        last = i

    return result 


words=["This", "is", "an", "example", "of", "text", "justification."]
L= 16

print justify(words, L)

