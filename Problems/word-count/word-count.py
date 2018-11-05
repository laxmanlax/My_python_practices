class wordcount:
    all_words={}
    def __init__(self, words):
        self.words = words
        self.word_count = self.word_count(words)

    def word_count(self, words):
        word_occurence = self.process_str(words)
        return word_occurence

    def process_str(self, words):
        chunks = words.split()
        for i in chunks:
            word =i
            count=0
            for l in chunks:
                if word == l:
                    count +=1

            self.all_words[word]=count
        return self.all_words


test = wordcount("rah rah ah ah ah\nroma roma ma\nga ga oh la la\n want your bad romance")
print test.words
print test.word_count
