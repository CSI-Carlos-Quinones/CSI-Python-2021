from multiprocessing.dummy import Array

class RandomHipsterStuff:
    def _init_(self,id,uid,word,words:Array,sentence,sentences:Array,paragraph,paragraphs:Array):
        self.id = id
        self.uid = uid
        self.word = word
        self.words = words
        self.sentence = sentence
        self.sentences = sentences
        self.paragraph = paragraph
        self.paragraphs = paragraphs


    